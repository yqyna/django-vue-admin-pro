from __future__ import print_function
import numpy as np
import pandas as pd


df = pd.read_excel("sales-funnel.xls")

sales_report = pd.pivot_table(df, index=["Manager", "Rep", "Product"], values=["Price", "Quantity"],
                              aggfunc=[np.sum, np.mean], fill_value=0)
# sales_report.head()

print(df[df["Product"] == "CPU"]["Quantity"].mean())
print(df[df["Product"] == "CPU"]["Price"].mean())
print(df[df["Product"] == "Software"]["Quantity"].mean())
print(df[df["Product"] == "Software"]["Price"].mean())

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"title": "Sales Funnel Report - National",
                 "national_pivot_table": sales_report.to_html()}
html_out = template.render(template_vars)
print(html_out)
# from django_weasyprint
# from weasyprint import HTML
# HTML(string=html_out).write_pdf("report.pdf")
# import wkhtmltopdf
# 导入库
import pdfkit

'''将字符串生成pdf文件'''


def str_to_pdf(string, to_file):
    # 将wkhtmltopdf.exe程序绝对路径传入config对象
    path_wkthmltopdf = r'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    # 生成pdf文件，to_file为文件路径
    pdfkit.from_string(string, to_file, configuration=config)
    print('完成')


str_to_pdf(html_out, 'out_3.pdf')

