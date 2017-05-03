# Author：zhaoyanqi

while True:

    list = ["查询", "添加", "删除", "退出"]
    for index, option in enumerate(list):
        print(index + 1, option)
    choice = input("input your choice:")

    if choice == "1":
        with open("haproxy", "r") as f1:
            r1 = f1.readlines()
            while True:
                search = input("输入域名来搜索,输入b返回，输入q退出:")
                if search == "q":
                    exit()
                elif search == "b":
                    break
                else:
                    c1 = 0
                    for index, line in enumerate(r1):
                        if line.strip() == "backend" + " " + search:
                            c1 = c1 + 1
                            print(r1[index + 1].strip())
                    if c1 == 0:
                        print("输入的域名不存在！")
    elif  choice == "2":
        while True:
            backend_update = input("请输入需要添加的域名,输入b返回，输入q退出：")
            if backend_update == "":
                print("不能为空")
                continue
            elif backend_update == "q":
                exit()
            elif backend_update == "b":
                break
            else:
                with open("haproxy", "r") as f2:
                    r2 = f2.readlines()
                    c2 = 0
                    for index, line in enumerate(r2):
                        #print(index,line)
                        if line.strip() == "backend" + " " + backend_update:
                            c2 = c2 + 1
                    #print(c2)
                    if c2 > 0:
                        print("输入的域名已经存在")
                    else:


                        # 读取模板并变成字典:
                        with open("add", "r+", encoding="utf-8") as f2:
                            a = str(f2.read())
                            b = eval(a)


                        # 修改字典内容:
                        b['backend'] = backend_update
                        while True:
                            server_update = input("请输入server的ip：")
                            if server_update == "":
                                print("不能为空")
                                continue
                            else:
                                b['record']['server'] = server_update
                                break
                        while True:
                            weight_update = input("请输入weight的值：")
                            if weight_update == "":
                                print("不能为空")
                                continue
                            else:
                                if weight_update.isdigit():
                                    b['record']['weight'] = int(weight_update)
                                    break
                                else:
                                    print("请输入数字")
                                    continue
                        while True:
                            maxconn_update = input("请输入maxconn的值：")
                            if maxconn_update == "":
                                print("不能为空")
                                continue
                            else:
                                if maxconn_update.isdigit():
                                    b['record']['maxconn'] = int(maxconn_update)
                                    break
                                else:
                                    print("请输入数字")
                                    continue


                        # 修改完的内容写入haproxy:
                        with open("haproxy", "a", encoding="utf-8") as f3:
                            f3.write("backend")
                            bakend_w = b.get("backend")
                            f3.write(" " + bakend_w)
                            t2 = b.get("record")
                            server_w = t2.get("server")
                            weight_w = t2.get("weight")
                            maxconn_w = t2.get("maxconn")
                            f3.write("\n" + "\t" + "\t")
                            f3.write("server" + " " + server_w + " " + "weight" + " " + str(weight_w) + " " + "maxconn" + " " + str(
                                maxconn_w) + "\n")
                            print("添加完成")
    elif choice == "3":
        while True:
            bankend_del = input("输入需要删除的域名,输入b返回，输入q退出:")
            if bankend_del == "q":
                exit()
            elif bankend_del == "b":
                break
            else:
                c_del = 0
                with open("haproxy", "r") as f_del:
                    r_del = f_del.readlines()
                    #print(r_del)
                    for index, line in enumerate(r_del):
                        if line.strip() == "backend" + " " + bankend_del:
                            c_del = + 1
                            r_del.pop(index + 1)
                            r_del.pop(index)
                            print("已删除！")
                    if c_del == 0:
                        print("输入的域名不存在！")
                with open("haproxy", "w") as f_w:
                    #print(r_del)
                    for line in r_del:
                        f_w.write(line)
    elif choice == "4":
        exit()
    else:
        print("请输入正确的选项！")



