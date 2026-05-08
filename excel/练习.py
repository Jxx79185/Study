from openpyxl import Workbook
import os 
import datetime
wb=Workbook()#实例化（创建工作簿）
sheet=wb.active#获取活动的工作表
sheet.title='kakaka'#为工作表改名
dit={
    '姓名':
        {'分数':'分数','班级':'班级'},
    '小明':
        {'分数':'100','班级':'二年级3班'},
    '小红':
        {'分数':'90','班级':'二年级2班'},
    '小刚':
        {'分数':'80','班级':'二年级5班'}
}
j=1
for i in dit:
    sheet[f'A{j}']=i
    sheet[f'B{j}']=dit[i]['分数']
    sheet[f'C{j}']=dit[i]['班级']
    j+=1
print(datetime.datetime.now())
sheet.append([datetime.datetime.now().strftime('%Y-%m-%d')])
wb.save('统计.xlsx')



# file_path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'test.xlsx')