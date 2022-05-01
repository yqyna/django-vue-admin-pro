# -*- coding: utf-8 -*-

"""
@author: 猿小天
@contact: QQ:1638245306
@Created on: 2021/8/9 009 20:48
@Remark:
"""
import os

from rest_framework import serializers

from dvadmin.system.models import ImgList
from dvadmin.utils.json_response import SuccessResponse, ErrorResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class ImgSerializer(CustomModelSerializer):
    img = serializers.SerializerMethodField(read_only=True)

    def get_img(self, instance):
        return str(instance.url)

    class Meta:
        model = ImgList
        fields = "__all__"

    def create(self, validated_data):
        validated_data['name'] = str(validated_data.get('url'))
        return super().create(validated_data)


class ImgViewSet(CustomModelViewSet):
    """
    图片管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = ImgList.objects.all()
    serializer_class = ImgSerializer
    filter_fields = ['name', ]
    permission_classes = []

    media_path = os.path.join('media/imgs/')

    def upload_file_chunk(self, request):

        media_path = self.media_path
        upload_file = request.FILES.get('file')
        real_file_name = request.data.get('name')
        if not all([upload_file, real_file_name]):
            return ErrorResponse(code=400, msg="分片上传缺少必传参数!")
        filename = upload_file.name
        image_uid, chunk = filename.split("_")
        chunk, file_type = chunk.split(',')
        img_obj = ImgList.objects.filter(image_uid=image_uid).first()
        if not all([image_uid, upload_file]):
            return ErrorResponse(code=400, msg="分片上传缺少必传参数!")
        if not img_obj:
            ImgList.objects.object.create(
                    name=real_file_name,
                    url="",
                    image_uid=image_uid,
                    md5sum=image_uid,
                    file_type=file_type
                )
            upload_file.save(f'{media_path}{filename}')
        else:
            if img_obj.is_success:
                return ErrorResponse(code=400, msg="该文件已经上传成功！")
            upload_file.save(f'{media_path}{filename}')
        return SuccessResponse(msg="分片上传成功", data={"filename": filename})

    def upload_success(self, request):
        image_uid = request.data.get('image_uid')  # 获取文件的唯一标识符
        if not all([image_uid]):
            return ErrorResponse(code=400, msg="缺少必传参数!")
        img_obj = ImgList.objects.filter(image_uid=image_uid).first()
        if not img_obj:
            return ErrorResponse(code=400, msg="该文件未进行分片上传！")
        target_filename = img_obj.image_uid + "." + img_obj.file_type

        chunk = 0  # 分片序号
        with open(f'{self.media_path}%s' % target_filename, 'wb') as target_file:  # 创建新文件
            while True:
                try:
                    filename = f'{self.media_path}%s_%d' % (image_uid, chunk)
                    source_file = open(filename, 'rb')  # 按序打开每个分片
                    target_file.write(source_file.read())  # 读取分片内容写入新文件
                    source_file.close()
                except IOError:
                    break
                chunk += 1
                os.remove(filename)
        img_obj.is_success = 1
        img_obj.url = f"media/imgs/{target_filename}"
        img_obj.save()
        return SuccessResponse(msg="上传成功", data=[])
