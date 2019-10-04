import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_demo.settings")
    import django
    django.setup()

    from app01 import models
    # ORM分组查询 每个部门名称及部门的平均工资

    # ret = models.Employee.objects.all()
    # """
    # SELECT `employee`.`id`, `employee`.`name`, `employee`.`age`, `employee`.`salary`, `employee`.`province`, `employee`.`dept` FROM `employee` LIMIT 21; args=()
    # """
    # print(ret)

    # ret = models.Employee.objects.all().values("dept", "age")
    # """
    # SELECT `employee`.`dept`, `employee`.`age` FROM `employee` LIMIT 21; args=()
    # """
    # print(ret)

    from django.db.models import Avg
    # ret = models.Employee.objects.values("province").annotate(a=Avg("salary")).values("province", "a")
    # """
    # SELECT `employee`.`province`, AVG(`employee`.`salary`) AS `a` FROM `employee` GROUP BY `employee`.`province` ORDER BY NULL LIMIT 21; args=()
    # """
    # print(ret)

    # ORM连表分组查询
    # ret = models.Person.objects.values("dept_id").annotate(a=Avg("salary")).values("dept__name", "a")
    # """
    # SELECT `dept`.`name`, AVG(`person`.`salary`) AS `a` FROM `person` INNER JOIN `dept` ON (`person`.`dept_id` = `dept`.`id`) GROUP BY `person`.`dept_id`, `dept`.`name` ORDER BY NULL LIMIT 21; args=()
    # """
    # print(ret)

    # 查询person表，判断每个人的工资是否大于2000
    # ret = models.Person.objects.all().extra(
    #     select={"gt": "salary > 2000"}
    # )
    #
    # """
    # SELECT (salary > 2000) AS `gt`, `person`.`id`, `person`.`name`, `person`.`salary`, `person`.`dept_id` FROM `person` LIMIT 21; args=()
    # """
    # # print(ret)
    # for i in ret:
    #     print(i.name, i.gt)


    # 执行原生的SQL语句
    from django.db import connection
    cursor = connection.cursor()  # 获取光标，等待执行SQL语句
    cursor.execute("""SELECT * from person where id = %s""", [1])
    row = cursor.fetchone()
    print(row)


#
#
# from django.db import models
# # Create your models here.
# class Employee(models.Model):
#     name = models.CharField(max_length=16, unique=True)
#     age = models.IntegerField()
#     salary = models.IntegerField()
#     province = models.CharField(max_length=32)
#     dept = models.CharField(max_length=16)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "employee"
#
#
# class Dept(models.Model):
#     """
#     部门表
#     """
#     name = models.CharField(max_length=16)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "dept"
#
# class Person(models.Model):
#     """
#     员工表
#     """
#     name = models.CharField(max_length=16)
#     salary = models.IntegerField()
#     dept = models.ForeignKey(to="Dept")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "person"
