# -*- coding: utf-8 -*-
"""
Task 5.3

The script should prompt the user for input:
* interface mode (access / trunk)
* interface number (Gi0 / 3)
* VLAN number (for trunk mode, a list of VLANs will be entered)

В зависимости от выбранного режима, на стандартный поток вывода, должна возвращаться
соответствующая конфигурация access или trunk (шаблоны команд находятся в списках
access_template и trunk_template).

При этом, сначала должна идти строка interface и подставлен номер интерфейса, а затем
соответствующий шаблон, в который подставлен номер VLANа (или список VLANов).

Restriction: All tasks must be done using the topics covered in this and previous chapters. То есть эту
задачу можно solved without using the if condition.и циклов for/while.

Подсказка:
Подводящим к этому заданию было задание 5.1. Чтобы было легче решить это задание,
можно посмотреть на задание 5.1 и разобраться как там получилось
вывести разную информацию в зависимости от ввода пользователя.

Ниже примеры выполнения скрипта, чтобы было проще понять задачу.

Пример выполнения скрипта, при выборе режима access:

$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): access
Введите тип и номер интерфейса: Fa0/6
Введите номер влан(ов): 3

interface Fa0/6
switchport mode access
switchport access vlan 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Пример выполнения скрипта, при выборе режима trunk:
$ python task_5_3.py
Введите режим работы интерфейса (access/trunk): trunk
Введите тип и номер интерфейса: Fa0/7
Введите номер влан(ов): 2,3,4,5

interface Fa0/7
switchport trunk encapsulation dot1q
switchport mode trunk
switchport trunk allowed vlan 2,3,4,5
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]
