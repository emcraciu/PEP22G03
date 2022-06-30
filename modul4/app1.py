def check_logs():
    users = []
    passwd = []
    for i in range(1, 4):
        users.append(input(f"User PC.{i}"))
        passwd.append(input(f"User password.{i}"))
    for i in range(3):
        print(f"{users[i]} --> {passwd[i]}")


check_logs()

angajat1 = {
    'nume': 'Ana-Maria Popescu',
    'departament': 'IT',
    'ID': 3409,
    'Salar': 4560,
}
angajat2 = {
    'nume': 'Marian Muntean',
    'departament': 'IT',
    'ID': 2235,
    'Salar': 4556,
}
angajat3 = {
    'nume': 'Maria Manea',
    'departament': 'HR',
    'ID': 1908,
    'Salar': 6755,
}
angajat4 = {
    'nume': 'Oana Popa',
    'departament': 'HR',
    'ID': 1977,
    'Salar': 5400,
}
angajat5 = {
    'nume': 'David Codru',
    'departament': 'Management',
    'ID': 1988,
    'Salar': 12900,
}
lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]
