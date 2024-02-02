import pymysql
import openpyxl

# 新增部门


def insert_dept(cursor):
    no = int(input('部门编号: '))
    name = input('部门名称: ')
    location = input('部门所在地: ')
    affected_rows = cursor.execute(
        'insert into `tb_dept` values (%s, %s, %s)',
        (no, name, location)
    )
    if affected_rows == 1:
        print('新增部门成功!!!')


# 删除部门
def delete_dept(cursor):
    no = int(input('部门编号: '))
    affected_rows = cursor.execute(
        'delete from `tb_dept` where `dno`=%s',
        (no, )
    )
    if affected_rows == 1:
        print('删除部门成功!!!')


# 更新部门，根据no
def update_dept(cursor):
    no = int(input('部门编号: '))
    name = input('部门名称: ')
    location = input('部门所在地: ')
    affected_rows = cursor.execute(
        'update `tb_dept` set `dname`=%s, `dloc`=%s where `dno`=%s',
        (name, location, no)
    )
    if affected_rows == 1:
        print('更新部门信息成功!!!')


# 查询部门
def select_dept(cursor):
    cursor.execute('select `dno`, `dname`, `dloc` from `tb_dept`')
    # 4. 通过游标对象抓取数据
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()


# 查询员工数据
def select_emp(cursor):
    page = int(input('页码: '))
    size = int(input('大小: '))
    cursor.execute(
        'select `eno`, `ename`, `job`, `sal` from `tb_emp` order by `sal` desc limit %s,%s',
        ((page - 1) * size, size)
    )
    # 4. 通过游标对象抓取数据
    for emp_dict in cursor.fetchall():
        print(emp_dict)


# 导出员工数据到Excel
def save_xl(cursor):
    # 创建工作簿对象
    workbook = openpyxl.Workbook()
    # 获得默认的工作表
    sheet = workbook.active
    # 修改工作表的标题
    sheet.title = '员工基本信息'
    # 给工作表添加表头
    sheet.append(('工号', '姓名', '职位', '月薪', '补贴', '部门'))
    cursor.execute(
        'select `eno`, `ename`, `job`, `sal`, coalesce(`comm`, 0), `dname` '
        'from `tb_emp` natural join `tb_dept`'
    )
    # 通过游标抓取数据
    row = cursor.fetchone()
    while row:
        # 将数据逐行写入工作表中
        sheet.append(row)
        row = cursor.fetchone()
    # 保存工作簿
    workbook.save('res/hrs.xlsx')


def main():
    # 1. 创建连接（Connection）
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='root', password='',
                           database='hrs', charset='utf8mb4')
    try:
        # 2. 获取游标对象（Cursor）
        with conn.cursor() as cursor:
            # 3. 通过游标对象向数据库服务器发出SQL语句
            # insert_dept(cursor)
            # delete_dept(cursor)
            # update_dept(cursor)
            # select_dept(cursor)
            # select_emp(cursor)
            save_xl(cursor)
        # 4. 提交事务（transaction）
        conn.commit()
    except pymysql.MySQLError as err:
        # 4. 回滚事务
        conn.rollback()
        print(type(err), err)
    finally:
        # 5. 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
