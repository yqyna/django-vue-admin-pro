# 初始化
import os

import django

from dvadmin.utils.core_initialize import CoreInitialize

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')
django.setup()

from dvadmin.system.models import Dept, Button, Menu, MenuButton, Role, Users
from dvadmin.system.util import init_area


class Initialize(CoreInitialize):
    creator_id = 1

    def init_dept(self):
        """
        初始化部门信息
        """
        self.dept_data = [
            {
                "id": 1,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "dvadmin团队",
                "sort": 1,
                "owner": None,
                "phone": None,
                "email": None,
                "status": 1,
                "creator_id": 1,
                "parent_id": None
            }
        ]
        self.save(Dept, self.dept_data, "部门信息")

    def init_button(self):
        """
        初始化按钮表
        """
        self.button_data = [
            {
                "id": 1,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "creator_id": 1
            },
            {
                "id": 2,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "creator_id": 1
            },
            {
                "id": 3,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "creator_id": 1
            },
            {
                "id": 4,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "详细",
                "value": "Retrieve",
                "creator_id": 1
            },
            {
                "id": 5,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "creator_id": 1
            },
            {
                "id": 6,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "保存",
                "value": "Save",
                "creator_id": 1
            }
        ]
        self.save(Button, self.button_data, "权限表标识")

    def init_menu(self):
        """
        初始化菜单表
        """
        self.menu_data = [
            {
                "id": 1,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "file-text",
                "name": "菜单管理",
                "sort": 1,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/menu",
                "component": "system/menu",
                "component_name": "menu",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 2,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "icon": "cogs",
                "name": "系统管理",
                "sort": 1,
                "is_link": 0,
                "is_catalog": 1,
                "web_path": None,
                "component": None,
                "component_name": None,
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": None
            },
            {
                "id": 3,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "users",
                "name": "用户管理",
                "sort": 4,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/user",
                "component": "system/user/index",
                "component_name": "user",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 4,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "address-book",
                "name": "角色管理",
                "sort": 6,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/role",
                "component": "system/role/index",
                "component_name": "role",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 5,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "icon": "bank",
                "name": "部门管理",
                "sort": 5,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/dept",
                "component": "system/dept/index",
                "component_name": "dept",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 6,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "key",
                "name": "角色权限",
                "sort": 7,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/rolePermission",
                "component": "system/rolePermission/index",
                "component_name": "rolePermission",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 7,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "dot-circle-o",
                "name": "菜单按钮",
                "sort": 2,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/menuButton",
                "component": "system/menuButton/index",
                "component_name": "menuButton",
                "status": 1,
                "cache": 0,
                "visible": 0,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 8,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "bullseye",
                "name": "按钮管理",
                "sort": 3,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/button",
                "component": "system/button/index",
                "component_name": "button",
                "status": 1,
                "cache": 0,
                "visible": 0,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 9,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "compass",
                "name": "接口白名单",
                "sort": 8,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/apiWhiteList",
                "component": "system/whiteList/index",
                "component_name": "whiteList",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 10,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "book",
                "name": "字典管理",
                "sort": 9,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/dictionary",
                "component": "system/dictionary/index",
                "component_name": "dictionary",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 11,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "map",
                "name": "地区管理",
                "sort": 10,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/areas",
                "component": "system/areas/index",
                "component_name": "areas",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 12,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "folder-open",
                "name": "附件管理",
                "sort": 11,
                "is_link": 0,
                "is_catalog": 1,
                "web_path": "",
                "component": "",
                "component_name": "",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 2
            },
            {
                "id": 13,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "file-text-o",
                "name": "文件管理",
                "sort": 12,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/file",
                "component": "system/fileList/file/index",
                "component_name": "file",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 12
            },
            {
                "id": 14,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "file-photo-o",
                "name": "图片管理",
                "sort": 13,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/img",
                "component": "system/fileList/img/index",
                "component_name": "img",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 12
            },
            {
                "id": 15,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "icon": "",
                "name": "日志管理",
                "sort": 16,
                "is_link": 0,
                "is_catalog": 1,
                "web_path": "",
                "component": None,
                "component_name": None,
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": None
            },
            {
                "id": 16,
                "description": "",
                "modifier": "1",
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "icon": "file-code-o",
                "name": "操作日志",
                "sort": 16,
                "is_link": 0,
                "is_catalog": 0,
                "web_path": "/operationLog",
                "component": "system/log/operationLog/index",
                "component_name": "operationLog",
                "status": 1,
                "cache": 0,
                "visible": 1,
                "creator_id": 1,
                "parent_id": 15
            }
        ]
        self.save(Menu, self.menu_data, "菜单表")

    def init_menu_button(self):
        """
        初始化菜单按钮表
        """
        self.menu_button_data = [
            {
                "id": 1,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "api": "/api/system/menu/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 1
            },
            {
                "id": 2,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "api": "/api/system/menu/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 1
            },
            {
                "id": 3,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "api": "/api/system/menu/",
                "method": 1,
                "creator_id": 1,
                "menu_id": 1
            },
            {
                "id": 4,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "详细",
                "value": "Retrieve",
                "api": "/api/system/menu/{id}/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 1
            },
            {
                "id": 5,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "api": "/api/system/menu/{id}/",
                "method": 3,
                "creator_id": 1,
                "menu_id": 1
            },
            {
                "id": 6,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "api": "/api/system/user/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 3
            },
            {
                "id": 7,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "api": "/api/system/user/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 3
            },
            {
                "id": 8,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "详细",
                "value": "Retrieve",
                "api": "/api/system/user/{id}/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 3
            },
            {
                "id": 9,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "api": "/api/system/user/",
                "method": 1,
                "creator_id": 1,
                "menu_id": 3
            },
            {
                "id": 10,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "api": "/api/system/user/{id}/",
                "method": 3,
                "creator_id": 1,
                "menu_id": 3
            },
            {
                "id": 11,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "api": "/api/system/role/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 4
            },
            {
                "id": 12,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "api": "/api/system/role/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 4
            },
            {
                "id": 13,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "详细",
                "value": "Retrieve",
                "api": "/api/system/role/{id}/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 4
            },
            {
                "id": 14,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "api": "/api/system/role/",
                "method": 1,
                "creator_id": 1,
                "menu_id": 4
            },
            {
                "id": 15,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "api": "/api/system/role/{id}/",
                "method": 3,
                "creator_id": 1,
                "menu_id": 4
            },
            {
                "id": 16,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "api": "/api/system/dept/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 5
            },
            {
                "id": 17,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "api": "/api/system/dept/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 5
            },
            {
                "id": 18,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "详细",
                "value": "Retrieve",
                "api": "/api/system/dept/{id}/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 5
            },
            {
                "id": 19,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "api": "/api/system/dept/",
                "method": 1,
                "creator_id": 1,
                "menu_id": 5
            },
            {
                "id": 20,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "api": "/api/system/dept/{id}/",
                "method": 3,
                "creator_id": 1,
                "menu_id": 5
            },
            {
                "id": 21,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "api": "/api/system/menu_button/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 7
            },
            {
                "id": 22,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "api": "/api/system/menu_button/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 7
            },
            {
                "id": 23,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "api": "/api/system/menu_button/",
                "method": 1,
                "creator_id": 1,
                "menu_id": 7
            },
            {
                "id": 24,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "api": "/api/system/menu_button/{id}/",
                "method": 3,
                "creator_id": 1,
                "menu_id": 7
            },
            {
                "id": 25,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "api": "/api/system/button/",
                "method": 1,
                "creator_id": 1,
                "menu_id": 8
            },
            {
                "id": 26,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "api": "/api/system/button/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 8
            },
            {
                "id": 27,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "api": "/api/system/button/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 8
            },
            {
                "id": 28,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "api": "/api/system/button/{id}/",
                "method": 3,
                "creator_id": 1,
                "menu_id": 8
            },
            {
                "id": 29,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "保存",
                "value": "Save",
                "api": "/api/system/role/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 6
            },
            {
                "id": 30,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "api": "/api/system/api_white_list/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 9
            },
            {
                "id": 31,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "api": "/api/system/api_white_list/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 9
            },
            {
                "id": 32,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "详细",
                "value": "Retrieve",
                "api": "/api/system/api_white_list/{id}/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 9
            },
            {
                "id": 33,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "api": "/api/system/api_white_list/",
                "method": 1,
                "creator_id": 1,
                "menu_id": 9
            },
            {
                "id": 34,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "api": "/api/system/api_white_list/{id}/",
                "method": 3,
                "creator_id": 1,
                "menu_id": 9
            },
            {
                "id": 35,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "api": "/api/system/dictionary/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 10
            },
            {
                "id": 36,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "api": "/api/system/dictionary/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 10
            },
            {
                "id": 37,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "详细",
                "value": "Retrieve",
                "api": "/api/system/dictionary/{id}/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 10
            },
            {
                "id": 38,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "api": "/api/system/dictionary/",
                "method": 1,
                "creator_id": 1,
                "menu_id": 10
            },
            {
                "id": 39,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "api": "/api/system/dictionary/{id}/",
                "method": 3,
                "creator_id": 1,
                "menu_id": 10
            },
            {
                "id": 40,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "编辑",
                "value": "Update",
                "api": "/api/system/area/{id}/",
                "method": 2,
                "creator_id": 1,
                "menu_id": 11
            },
            {
                "id": 41,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "查询",
                "value": "Search",
                "api": "/api/system/area/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 11
            },
            {
                "id": 42,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "详细",
                "value": "Retrieve",
                "api": "/api/system/area/{id}/",
                "method": 0,
                "creator_id": 1,
                "menu_id": 11
            },
            {
                "id": 43,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "新增",
                "value": "Create",
                "api": "/api/system/area/",
                "method": 1,
                "creator_id": 1,
                "menu_id": 11
            },
            {
                "id": 44,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "删除",
                "value": "Delete",
                "api": "/api/system/area/{id}/",
                "method": 3,
                "creator_id": 1,
                "menu_id": 11
            }
        ]
        self.save(MenuButton, self.menu_button_data, "菜单按钮表")

    def init_role(self):
        """
        初始化角色表
        """
        data = [
            {
                "id": 1,
                "description": None,
                "modifier": "1",
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "name": "管理员",
                "key": "admin",
                "sort": 1,
                "status": 1,
                "admin": 1,
                "data_range": 3,
                "menu": [ele.get("id") for ele in self.menu_data],
                "permission": [ele.get("id") for ele in self.menu_button_data],
                "remark": None,
                "creator_id": 1
            }
        ]
        self.save(Role, data, "角色表")

    def init_users(self):
        """
        初始化用户表
        """
        data = [
            {
                "password": "pbkdf2_sha256$260000$g17x5wlSiW1FZAh1Eudchw$ZeSAqj3Xak0io8v/pmPW0BX9EX5R2zFXDwbbD68oBFk=",
                "last_login": None,
                "is_superuser": 1,
                "first_name": "",
                "last_name": "",
                "is_staff": 1,
                "is_active": 1,
                "id": 1,
                "description": None,
                "modifier": None,
                "dept_belong_id": None,
                "update_datetime": "",
                "create_datetime": "",
                "username": "superadmin",
                "email": "1638245306@qq.com",
                "mobile": None,
                "avatar": None,
                "name": "超级管理员",
                "gender": 1,
                "creator_id": None,
                "dept_id": 1
            },
            {
                "password": "pbkdf2_sha256$260000$g17x5wlSiW1FZAh1Eudchw$ZeSAqj3Xak0io8v/pmPW0BX9EX5R2zFXDwbbD68oBFk=",
                "last_login": None,
                "is_superuser": 0,
                "first_name": "",
                "last_name": "",
                "is_staff": 1,
                "is_active": 1,
                "id": 2,
                "description": "",
                "modifier": None,
                "dept_belong_id": "",
                "update_datetime": "",
                "create_datetime": "",
                "username": "admin",
                "email": "1@qq.com",
                "mobile": "",
                "avatar": "",
                "name": "管理员",
                "gender": 1,
                "creator_id": None,
                "dept_id": 1,
                "role": [1],
            }
        ]
        self.save(Users, data, "用户表", no_reset=True)

    def run(self):
        self.init_dept()
        self.init_button()
        self.init_menu()
        self.init_menu_button()
        self.init_role()
        self.init_users()
        init_area.main()  # 初始化地区数据


# 项目init 初始化，默认会执行 main 方法进行初始化
def main(reset=False):
    Initialize(reset).run()
    pass


if __name__ == '__main__':
    main()
