import os
print("ARGV Helper by jerbear64 and Jhynjhiruu")
if not os.path.exists("dsiware"):os.mkdir("dsiware")
apps = [os.path.join(".", o) for o in os.listdir(".")][:-2]
for app in range(len(apps)):
    appID = apps[app][-8:]
    try:appName = next(os.walk(appID + "/content/"))[2][0]
    except:break
    print("Found app at /{0}/content/{1}\nGenerating argv...".format(appID, appName))
    with open("dsiware/{}.argv".format(appID), "w") as argv:argv.write("sd:/title/00030004/" + appID + "/content/" + appName)
print("Generated argvs for {} file(s) successfully".format(app))
