from androguard import misc


def getPermission(apk):
    for permission in apk.get_permissions():
        print(permission)


def getPermissionDetails(apk):
    for detail_key in apk.get_details_permissions():
        detail_value_list = apk.get_details_permissions()[detail_key]
        print("----------------------------")
        print("Permission" + detail_key)
        for detail_value in detail_value_list:
            print(detail_value)

        print("----------------------------")







if __name__ == '__main__':
	main()
