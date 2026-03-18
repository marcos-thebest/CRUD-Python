# ᴄʀᴜᴅ ɪɴ ᴘʏᴛʜᴏɴ
def menu():
    print("\n1️⃣  - ​🇨​​🇷​​🇪​​🇦​​🇹​​🇪​\n2️⃣  - ​🇷​​🇪​​🇦​​🇩​\n3️⃣  - ​🇺​​🇵​​🇩​​🇦​​🇹​​🇪​\n4️⃣  - ​🇩​​🇪​​🇱​​🇪​​🇹​​🇪​\n5️⃣  - ​🇪​​🇽​​🇮​​🇹​ ​🇹​​🇭​​🇪​ ​🇵​​🇷​​🇴​​🇬​​🇷​​🇦​​🇲​")

# ᴄʀᴇᴀᴛɪɴɢ ᴀɴ ᴇᴍᴘᴛʏ ʟɪꜱᴛ ꜰᴏʀ ᴍʏ “ᴄʀᴇᴀᴛᴇ”
listCreatePeople = []

while True:

    menu()
    opction = int(input("\n​🇸​ᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇꜱɪʀᴇᴅ ᴍᴇɴᴜ ᴏᴘᴛɪᴏɴ: "))

    # ᴠᴀʟɪᴅᴀᴛɪɴɢ ᴛʜᴇ ᴜꜱᴇʀ'ꜱ ᴏᴘᴛɪᴏɴ
    while (opction < 1) or (opction > 5):
        print("\nᴇʀʀᴏʀ - ɪɴᴠᴀʟɪᴅ ᴏᴘᴛɪᴏɴ - ᴘʟᴇᴀꜱᴇ ᴛʀʏ ᴀɢᴀɪɴ!")
        opction = int(input("\n​🇸​ᴇʟᴇᴄᴛ ᴛʜᴇ ᴅᴇꜱɪʀᴇᴅ ᴍᴇɴᴜ ᴏᴘᴛɪᴏɴ: "))

    # ᴘʀᴏᴄᴇssɪɴɢ ᴛʜᴇ ᴜꜱᴇʀ'ꜱ ᴏᴘᴛɪᴏɴ
    if (opction == 1):
        print("\n══════ஜ ​🇨​​🇷​​🇪​​🇦​​🇹​​🇪​ ஜ══════")
        try:
            name = input("\n​🇪​​🇳​​🇹​​🇪​​🇷​ ​🇾​​🇴​​🇺​​🇷​ ​🇳​​🇦​​🇲​​🇪​: ")
            age = int(input("\n​🇪​​🇳​​🇹​​🇪​​🇷​ ​🇾​​🇴​​🇺​​🇷​ ​🇦​​🇬​​🇪​: "))
            height = float(input("\n​🇪​​🇳​​🇹​​🇪​​🇷​ ​🇾​​🇴​​🇺​​🇷​ ​🇭​​🇪​​🇮​​🇬​​🇭​​🇹​: "))
            salary = float(input("\n​🇪​​🇳​​🇹​​🇪​​🇷​ ​🇾​​🇴​​🇺​​🇷​ ​🇸​​🇦​​🇱​​🇦​​🇷​​🇾​: "))

        except ValueError:
            print("\nɪ ᴏɴʟʏ ᴀᴄᴄᴇᴘᴛ ᴡʜᴏʟᴇ ɴᴜᴍʙᴇʀꜱ ꜰᴏʀ ᴀɢᴇ!")

        except FloatingPointError:
            print("\nɪ ᴏɴʟʏ ᴀᴄᴄᴇᴘᴛ ᴅᴇᴄɪᴍᴀʟ ɴᴜᴍʙᴇʀꜱ ꜰᴏʀ ʜᴇɪɢʜᴛ ᴀɴᴅ ꜱᴀʟᴀʀʏ!")

        else:
            dictionaryPerson = {
                "Name":name,
                "Age":age,
                "Height":height,
                "Salary":salary
            }
            listCreatePeople.append(dictionaryPerson)
            print("\n​🇾​​🇴​​🇺​ ​🇭​​🇦​​🇻​​🇪​ ​🇧​​🇪​​🇪​​🇳​ ​🇸​​🇺​​🇨​​🇨​​🇪​​🇸​​🇸​​🇫​​🇺​​🇱​​🇱​​🇾​ ​🇷​​🇪​​🇬​​🇮​​🇸​​🇹​​🇪​​🇷​​🇪​​🇩​!")

    elif (opction == 2):
        print("\n══════ஜ ​🇷​​🇪​​🇦​​🇩​ ஜ══════")

        if len(listCreatePeople) == 0:
            print("\n​🇳​​🇴​ ​🇴​​🇳​​🇪​ ​🇼​​🇦​​🇸​ ​🇫​​🇴​​🇺​​🇳​​🇩​!")

        else:
            accountant = 0

            for person in listCreatePeople:
                print(f"\n{accountant} - {person["Name"]}")
                accountant += 1

    elif (opction == 3):
        print("\n══════ஜ ​🇺​​🇵​​🇩​​🇦​​🇹​​🇪​ ஜ══════")

        if len(listCreatePeople) == 0:
            print("\n​🇳​​🇴​ ​🇴​​🇳​​🇪​ ​🇼​​🇦​​🇸​ ​🇫​​🇴​​🇺​​🇳​​🇩​!")

        else:
            accountant = 0

            for person in listCreatePeople:
                print(f"\n{accountant} - {person["Name"]}")
                accountant += 1

            index = int(input("\nᴇɴᴛᴇʀ ᴛʜᴇ ɪᴅ ᴏꜰ ᴛʜᴇ ᴘᴇʀꜱᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴇᴅɪᴛ: "))

            try:
                new_name = input("\n​🇪​​🇳​​🇹​​🇪​​🇷​ ​🇹​​🇭​​🇪​ ​🇳​​🇪​​🇼​ ​🇳​​🇦​​🇲​​🇪​: ")
                new_age = int(input("\n​🇪​​🇳​​🇹​​🇪​​🇷​ ​🇹​​🇭​​🇪​ ​🇳​​🇪​​🇼​ ​🇦​​🇬​​🇪​: "))
                new_height = float(input("\n​🇪​​🇳​​🇹​​🇪​​🇷​ ​🇹​​🇭​​🇪​ ​🇳​​🇪​​🇼​ ​🇭​​🇪​​🇮​​🇬​​🇭​​🇹​: "))
                new_salary = float(input("\n​🇪​​🇳​​🇹​​🇪​​🇷​ ​🇹​​🇭​​🇪​ ​🇳​​🇪​​🇼​ ​🇸​​🇦​​🇱​​🇦​​🇷​​🇾​: "))

            except ValueError:
                print("\n​🇮​ ​🇴​​🇳​​🇱​​🇾​ ​🇦​​🇨​​🇨​​🇪​​🇵​​🇹​ ​🇼​​🇭​​🇴​​🇱​​🇪​ ​🇳​​🇺​​🇲​​🇧​​🇪​​🇷​​🇸​ ​🇫​​🇴​​🇷​ ​🇦​​🇬​​🇪​!")

            except FloatingPointError:
                print("\n​🇮​ ​🇴​​🇳​​🇱​​🇾​ ​🇦​​🇨​​🇨​​🇪​​🇵​​🇹​ ​🇩​​🇪​​🇨​​🇮​​🇲​​🇦​​🇱​ ​🇳​​🇺​​🇲​​🇧​​🇪​​🇷​​🇸​ ​🇫​​🇴​​🇷​ ​🇭​​🇪​​🇮​​🇬​​🇭​​🇹​ ​🇦​​🇳​​🇩​ ​🇸​​🇦​​🇱​​🇦​​🇷​​🇾​!")

            else:
                listCreatePeople[index]["Name"] = new_name
                listCreatePeople[index]["Age"] = new_age
                listCreatePeople[index]["Height"] = new_height
                listCreatePeople[index]["Salary"] = new_salary
                
                print("\n​🇹​​🇭​​🇪​ ​🇵​​🇪​​🇷​​🇸​​🇴​​🇳​ ​🇭​​🇦​​🇸​ ​🇧​​🇪​​🇪​​🇳​ ​🇸​​🇺​​🇨​​🇨​​🇪​​🇸​​🇸​​🇫​​🇺​​🇱​​🇱​​🇾​ ​🇺​​🇵​​🇩​​🇦​​🇹​​🇪​​🇩​ ​🇮​​🇳​ ​🇹​​🇭​​🇪​ ​🇸​​🇾​​🇸​​🇹​​🇪​​🇲​!")

    elif (opction == 4):
        print("\n══════ஜ ᴅᴇʟᴇᴛᴇ ஜ══════")

        if len(listCreatePeople) == 0:
            print("\n​🇳​​🇴​ ​🇴​​🇳​​🇪​ ​🇼​​🇦​​🇸​ ​🇫​​🇴​​🇺​​🇳​​🇩​!")

        else:
            accountant = 0

            for person in listCreatePeople:
                print(f"\n{accountant} - {person["Name"]}")
                accountant += 1

            index = int(input("\nᴇɴᴛᴇʀ ᴛʜᴇ ɪᴅ ᴏꜰ ᴛʜᴇ ᴘᴇʀꜱᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ: "))

            listCreatePeople.remove(person)

            print("\n​🇺​​🇸​​🇪​​🇷​ ​🇸​​🇺​​🇨​​🇨​​🇪​​🇸​​🇸​​🇫​​🇺​​🇱​​🇱​​🇾​ ​🇩​​🇪​​🇱​​🇪​​🇹​​🇪​​🇩​ ​🇫​​🇷​​🇴​​🇲​ ​🇹​​🇭​​🇪​ ​🇸​​🇾​​🇸​​🇹​​🇪​​🇲​!")

    else:
        print("\n══════ஜ ​🇱​​🇪​​🇦​​🇻​​🇮​​🇳​​🇬​ ​🇹​​🇭​​🇪​ ​🇸​​🇾​​🇸​​🇹​​🇪​​🇲​ ஜ══════\n")
        break