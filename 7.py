# -*- coding: utf-8 -*-
'''
© Warbot v`1
'''
from important import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from random import randint
from multiprocessing import Pool, Process

# Setup
parser = argparse.ArgumentParser(description='© Warbot v`1')
parser.add_argument('-t', '--token', type=str, metavar='', required=False, help='Token | Example : Exxxx')
parser.add_argument('-e', '--email', type=str, default='', metavar='', required=False, help='Email Address | Example : example@xxx.xx')
parser.add_argument('-p', '--passwd', type=str, default='', metavar='', required=False, help='Password | Example : xxxx')
parser.add_argument('-a', '--appName', type=str, default='', metavar='', required=False, choices=list(ApplicationType._NAMES_TO_VALUES), help='Application Type | Example : CLOVAFRIENDS')
parser.add_argument('-s', '--systemname', type=str, default='', metavar='', required=False, help='System Name | Example : Clovafriens')
parser.add_argument('-c', '--channelid', type=str, default='', metavar='', required=False, help='Channel ID | Example : 1341209950')
parser.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
parser.add_argument('-S', '--showqr', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Show QR | Use : True/False')
args = parser.parse_args()
Bot_startTime = time.strftime("%H:%M:%S", time.localtime())
# Login line
print("""
\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m[ %s Start Bot ]\033[0m    
"""%(Bot_startTime))
cl = LINE("vjc23510@eoopy.com","mai065558mai")
cl.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
#========================Token1===================================================#
ka = LINE("unx95351@bcaoo.com","mai065558mai")
ka.log("Auth Token : " + str(ka.authToken))
channelToken = ka.getChannelResult()
#========================Token2===================================================#
kb = LINE("zdl30288@bcaoo.com","mai065558mai")
kb.log("Auth Token : " + str(kb.authToken))
channelToken = kb.getChannelResult()
#========================Token3===================================================#
kc = LINE("hul21174@bcaoo.com","mai065558mai")
kc.log("Auth Token : " + str(kc.authToken))
channelToken = kc.getChannelResult()
#========================Token4===================================================#
kd = LINE("isy89587@bcaoo.com","mai065558mai")
kd.log("Auth Token : " + str(kd.authToken))
channelToken = kd.getChannelResult()
#========================Token5===================================================#
ke = LINE("teq36085@eoopy.com","mai065558mai")
ke.log("Auth Token : " + str(ke.authToken))
channelToken = ke.getChannelResult()
#========================Token6===================================================#
kf = LINE("nva04145@bcaoo.com","mai065558mai")
kf.log("Auth Token : " + str(kf.authToken))
channelToken = kf.getChannelResult()
#========================Tokenjs===================================================#
k7 = LINE("tlq24537@bcaoo.com","mai065558mai")
k7.log("Auth Token : " + str(k7.authToken))
channelToken = k7.getChannelResult()
#========================8===================================================#
ajs = LINE("uep11978@cuoly.com","mai065558mai")
ajs.log("Auth Token : " + str(kf.authToken))
channelToken = ajs.getChannelResult()
#==============•••••••••••••••••   BOT WAR V`1 BY TEAM BOT PROTECT •••••••••••••••==============#
print("""\033["""+str(randint(0,1))+""";"""+str(randint(31,36))+"""m

	    WELCOME TO SELFBOT PROTECT WAR V'1 BY MAI
	
	
███████████████████████████████████
	
▀▀█▀▀ █▀▀ █▀▀█ █▀▄▀█ 
░▒█░░ █▀▀ █▄▄█ █░▀░█ 
░▒█░░ ▀▀▀ ▀░░▀ ▀░░░▀ 

▒█▀▀█ ▒█▀▀▀█ ▀▀█▀▀ 
▒█▀▀▄ ▒█░░▒█ ░▒█░░ 
▒█▄▄█ ▒█▄▄▄█ ░▒█░░ 

▒█▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █▀▀ █▀▀ ▀▀█▀▀ 
▒█▄▄█ █▄▄▀ █░░█ ░░█░░ █▀▀ █░░ ░░█░░ 
▒█░░░ ▀░▀▀ ▀▀▀▀ ░░▀░░ ▀▀▀ ▀▀▀ ░░▀░░ 

███████████████████████████████████
	
Login Time %s \033[0m\n\n"""%(Bot_startTime))
print ("Proses login sucsess")

call = cl
oepoll = OEPoll(cl)
team1=[ka,kb,kc,kd,ke,kf,k7]
team2=[ka,kb,kc,kd,ke,kf,k7]
team3=[ka,kb,kc,kd,ke,kf,k7]
team4=[ka,kb,kc,kd,ke,kf,k7]
team5=[ka,kb,kc,kd,ke,kf,k7]
team6=[ka,kb,kc,kd,ke,kf,k7]
team7=[ka,kb,kc,kd,ke,kf,k7]
team8=[ka,kb,kc,kd,ke,kf,k7]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid
Bmid = kb.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Fmid = kf.getProfile().mid
K7mid = k7.getProfile().mid
JSmid = ajs.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,K7mid]
ownerbot = ["u094af42f3bef6bac2e66ea53071d01b8","u46972f7c43e399c93cf49fad40ae7262"]
DHENZA = ["u094af42f3bef6bac2e66ea53071d01b8","u46972f7c43e399c93cf49fad40ae7262"]
TEAM = Bots+ownerbot+DHENZA
msg_dict = {}
msg_dict1 = {}
#==============[ Main Json ]==============#
wait = {"blacklist": {}}
main = codecs.open("DZwait.json","r","utf-8")
DZwait = json.load(main)
boters = codecs.open("DZbot.json","r","utf-8")
DZbot = json.load(boters)

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
warmode = []

settings = {
    "groupgambar":False,
    "changegambar":False,
    "modewar":True,
    "likeStat":True,
    "LikeOn":True,
    "Jscancel":True,
    "like":4,
    "autoJoinTicket":True,
    "keyCommand": "",
    "postingan":{},
    "Picture":False,
    "group":{},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

with open('TBP.json', 'r') as fp:
    DHENZA = json.load(fp)
listTimeLiking = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > timedelta(1):
            del msg_dict1[msg_id]

def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def atend1():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)


def cek(mid):
    if mid in (Bots):
        return True
    else:
        return False

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def sendMessage(to, Message, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes._from = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :「Gaje Bots」  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@teambotprotect "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def sendMention2(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(DZwait["keyCmd"]):
        cmd = pesan.replace(DZwait["keyCmd"],"")
    else:
        cmd = "command"
    return cmd
    
def helpbot():
    num = 1
    key = settings["keyCommand"]
    key = key.title()
    helpMessage2 = "╭━━━━━━━━━━━━━━━━\n"
    helpMessage2 += "│┃ " + "╭───⍟ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ⍟─\n"
    helpMessage2 += "│┃" + " ├───ᴄᴏᴍᴍᴀɴᴅ ᴋɪᴄᴋᴇʀ────────────\n"
    helpMessage2 += "│┃" + " ├──────────────\n"
    helpMessage2 += "│╠❂➣ %i. " % num + key + "on/off\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "mod on/off\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Set\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "join on/off \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ออน \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "รี\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ลบแชทคิก \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ลบแชท \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Mid \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Token \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Speed / sp \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Reboot \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "upg\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "up\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "1/7up\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "name: \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "1/6name: \n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Iv\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Contact (mid)\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Idcontact (tag)\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "js in/lv\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "มา/in\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ออก/out\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Bye\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Bk1/6 @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "clcancelall\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "cancelall\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i ." % num + key + " @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + " @\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + " b\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Clear bot\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Fresh\n"
    num = (num+1)    
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Banlist /ck\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Clearban/bc\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "/บิน\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "รายชื่อกลุ่ม\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Ivme (ใส่เลขกลุ่ม)\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Leavegroup (ใส่เลขกลุ่ม)\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "/บิน (for kickall)\n"
    num = (num+1)
    helpMessage2 += "│┃ " + "├──────────────\n"
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Proqr on/off\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Proinvite on/off\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Prokick on/off\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Projoin on/off\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Procancel on/off\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Protect on/off\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Js on/off\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "ck js\n"
    num = (num+1)
    helpMessage2 += "│╠❂➣ %i. " % num + key + "Iv js\n"
    num = (num+1)
    helpMessage2 += "│┃ " + "├──────────────\n"
    helpMessage2 += "│┃ " + "╰──⍟ ᴛᴇᴀᴍ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ⍟────────\n"
    helpMessage2 += "╰━━━━━━━━━━━━━━━━"
    helpMessage2 += " My ID LINE : 〘 https://line.me/ti/p/~gomaimaigo 〙\n"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 11:
            if op.param1 in protectqr:
                if op.param2 in TEAM or op.param2 in DZbot["Bots"] or op.param2 in DZbot["admin"]:pass
                else:
                    Z = cl.getGroup(op.param1)
                    if Z.preventedJoinByTicket == False:
                        Z.preventedJoinByTicket = True
                        random.choice(team1).updateGroup(Z)
                        random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                    else:
                        random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
            if op.param2 in wait["blacklist"]:
                G = cl.getGroup(op.param1)
                if G.preventedJoinByTicket == False:
                    G.preventedJoinByTicket = True
                    random.choice(team2).updateGroup(G)
                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                else:
                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])                              
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param3 not in TEAM and op.param3 not in DZbot["Bots"] and op.param3 not in DZbot["admin"]:
                    try:
                        ka.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kb.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kd.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
            if op.param3 in wait["blacklist"]:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    try:
                        ka.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kb.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kd.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
                else:pass
            if op.param3 in wait["blacklist"]:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.cancelGroupInvitation(op.param1,[op.param2])
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.cancelGroupInvitation(op.param1,[op.param2])
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.cancelGroupInvitation(op.param1,[op.param2])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.cancelGroupInvitation(op.param1,[op.param2])
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.cancelGroupInvitation(op.param1,[op.param2])
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.cancelGroupInvitation(op.param1,[op.param2])
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                else:pass
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                    cl.reissueGroupTicket(op.param1)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    warmode.append(op.param1)
                else:pass
        if op.type == 32:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 32:
            if op.param3 in TEAM or op.param3 in DZbot["Bots"] or op.param3 in DZbot["admin"]:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                                k7.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(team2).inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(team2).inviteIntoGroup(op.param1,[op.param3])
                else:pass                    
        if op.type == 19:
                if mid in op.param3:
                    if op.param2 not in TEAM and op.param3 not in DZbot["Bots"] and op.param3 not in DZbot["admin"]:
                        try:
                            ajs.acceptGroupInvitation(op.param1)                                                                     
                            G = ajs.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ajs.updateGroup(G)
                            Ticket = ajs.reissueGroupTicket(op.param1)
                            ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)	
                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)	                            
                            wait["blacklist"][op.param2] = True
                            ajs.leaveGroup(op.param1)
                            cl.inviteIntoGroup(op.param1,[JSmid])
                            cl.findAndAddContactsByMid(["u094af42f3bef6bac2e66ea53071d01b8"])
                            cl.inviteIntoGroup(op.param1,["u094af42f3bef6bac2e66ea53071d01b8"]) 
                            random.choice(Bots).inviteIntoGroup([JSmid])                           
                        except:
                            pass   
                            
        if op.type == 19:
            if op.param1 in protectantijs:
                if mid in op.param3:
                    if op.param2 not in TEAM and op.param3 not in DZbot["Bots"] and op.param3 not in DZbot["admin"]:
                        try:
                            ajs.acceptGroupInvitation(op.param1)                                                                                
                            G = ajs.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ajs.updateGroup(G)
                            Ticket = ajs.reissueGroupTicket(op.param1)
                            ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)	
                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                            k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)	                            
                            wait["blacklist"][op.param2] = True
                            ajs.leaveGroup(op.param1)
                            cl.inviteIntoGroup(op.param1,[JSmid])
                            cl.findAndAddContactsByMid(["u618e2d58baf46520bf8da7890edc5029"])
                            cl.inviteIntoGroup(op.param1,["u618e2d58baf46520bf8da7890edc5029"]) 
                            random.choice(Bots).inviteIntoGroup([JSmid])                           
                        except:
                            pass
                            
            if op.param3 in JSmid:
                if op.param3 not in TEAM and op.param3 not in DZbot["Bots"] and op.param3 not in DZbot["admin"]:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[JSmid])
                        cl.sendMessage(op.param1,"ANTI KICKER STAY")
                else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[JSmid])
                        cl.sendMessage(op.param1,"ANTI KICKER STAY")
                        
                if op.param3 not in TEAM and op.param3 not in DZbot["Bots"] and op.param3 not in DZbot["admin"]: 
                    if op.param3 in Owner:
                        if op.param1 in protectantijs:
                            wiat["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            cl.sendMessage(op.param1,"SUCSESS INVITE ADMIN")
                else:
                    pass
                   
        if op.type == 19:
            if mid in op.param3:
                if op.param2 not in TEAM and op.param2 not in Bots and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,Bots)
                        cl.acceptGroupInvitation(op.param1)
                        kb.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,Bots)
                            cl.acceptGroupInvitation(op.param1)
                            kc.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,Bots)
                                cl.acceptGroupInvitation(op.param1)
                                kd.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,Bots)
                                    cl.acceptGroupInvitation(op.param1)
                                    ke.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,Bots)
                                        cl.acceptGroupInvitation(op.param1)
                                        kf.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.inviteIntoGroup(op.param1,Bots)
                                            cl.acceptGroupInvitation(op.param1)
                                            k7.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                                k7.inviteIntoGroup(op.param1,Bots)
                                                cl.acceptGroupInvitation(op.param1)
                                                ka.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(team2).inviteIntoGroup(op.param1,Bots)
                                                    cl.acceptGroupInvitation(op.param1)
                                                    random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                    random.choice(team2).inviteIntoGroup(op.param1,Bots)
                                                    cl.acceptGroupInvitation(op.param1)
                                                    random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
                else:pass
                return
            if Amid in op.param3:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,Bots)
                        ka.acceptGroupInvitation(op.param1)
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,Bots)
                            ka.acceptGroupInvitation(op.param1)
                            kd.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,Bots)
                                ka.acceptGroupInvitation(op.param1)
                                ke.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.inviteIntoGroup(op.param1,Bots)
                                    ka.acceptGroupInvitation(op.param1)
                                    kf.cancelGroupInvitation(op.param1,[op.param2])                  
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,Bots)
                                        ka.acceptGroupInvitation(op.param1)
                                        k7.cancelGroupInvitation(op.param1,[op.param2])                     
                                    except:
                                        try:
                                            k7.kickoutFromGroup(op.param1,[op.param2])
                                            k7.inviteIntoGroup(op.param1,Bots)
                                            ka.acceptGroupInvitation(op.param1)
                                            kb.cancelGroupInvitation(op.param1,[op.param2])                     
                                        except:
                                            try:
                                                random.choice(team3).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team3).inviteIntoGroup(op.param1,Bots)
                                                ka.acceptGroupInvitation(op.param1)
                                                random.choice(team3).cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                random.choice(team3).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team3).inviteIntoGroup(op.param1,Bots)
                                                ka.acceptGroupInvitation(op.param1)
                                                random.choice(team3).cancelGroupInvitation(op.param1,[op.param2])
                else:pass
                return
            if Bmid in op.param3:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,Bots)
                        kb.acceptGroupInvitation(op.param1)
                        kd.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,Bots)
                            kb.acceptGroupInvitation(op.param1)
                            ke.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,Bots)
                                kb.acceptGroupInvitation(op.param1)
                                kf.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    kf.inviteIntoGroup(op.param1,Bots)
                                    kb.acceptGroupInvitation(op.param1)
                                    k7.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        k7.kickoutFromGroup(op.param1,[op.param2])
                                        k7.inviteIntoGroup(op.param1,Bots)
                                        kb.acceptGroupInvitation(op.param1)
                                        ka.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                            ka.inviteIntoGroup(op.param1,Bots)
                                            kb.acceptGroupInvitation(op.param1)
                                            kc.cancelGroupInvitation(op.param1,[op.param2])                     
                                        except:
                                            try:
                                                random.choice(team4).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team4).inviteIntoGroup(op.param1,Bots)
                                                kb.acceptGroupInvitation(op.param1)
                                                random.choice(team4).cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                random.choice(team4).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team4).inviteIntoGroup(op.param1,Bots)
                                                kb.acceptGroupInvitation(op.param1)
                                                random.choice(team4).cancelGroupInvitation(op.param1,[op.param2])
                else:pass
                return
            if Cmid in op.param3:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,Bots)
                        kc.acceptGroupInvitation(op.param1)
                        ke.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,Bots)
                            kc.acceptGroupInvitation(op.param1)
                            kf.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,Bots)
                                kc.acceptGroupInvitation(op.param1)
                                k7.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                    k7.inviteIntoGroup(op.param1,Bots)
                                    kc.acceptGroupInvitation(op.param1)
                                    ka.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                        ka.inviteIntoGroup(op.param1,Bots)
                                        kc.acceptGroupInvitation(op.param1)
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.inviteIntoGroup(op.param1,Bots)
                                            kc.acceptGroupInvitation(op.param1)
                                            kd.cancelGroupInvitation(op.param1,[op.param2])                     
                                        except:
                                            try:
                                                random.choice(team5).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team5).inviteIntoGroup(op.param1,Bots)
                                                kc.acceptGroupInvitation(op.param1)
                                                random.choice(team5).cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                random.choice(team5).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team5).inviteIntoGroup(op.param1,Bots)
                                                kc.acceptGroupInvitation(op.param1)
                                                random.choice(team5).cancelGroupInvitation(op.param1,[op.param2])
                else:pass
                return
            if Dmid in op.param3:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,Bots)
                        kd.acceptGroupInvitation(op.param1)
                        kf.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kf.kickoutFromGroup(op.param1,[op.param2])
                            kf.inviteIntoGroup(op.param1,Bots)
                            kd.acceptGroupInvitation(op.param1)
                            k7.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                k7.kickoutFromGroup(op.param1,[op.param2])
                                k7.inviteIntoGroup(op.param1,Bots)
                                kd.acceptGroupInvitation(op.param1)
                                ka.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,Bots)
                                    kd.acceptGroupInvitation(op.param1)
                                    kb.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,Bots)
                                        kd.acceptGroupInvitation(op.param1)
                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,Bots)
                                            kd.acceptGroupInvitation(op.param1)
                                            ke.cancelGroupInvitation(op.param1,[op.param2])                     
                                        except:
                                            try:
                                                random.choice(team6).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team6).inviteIntoGroup(op.param1,Bots)
                                                kd.acceptGroupInvitation(op.param1)
                                                random.choice(team6).cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                random.choice(team6).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team6).inviteIntoGroup(op.param1,Bots)
                                                kd.acceptGroupInvitation(op.param1)
                                                random.choice(team6).cancelGroupInvitation(op.param1,[op.param2])
                else:pass
                return
            if Emid in op.param3:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.inviteIntoGroup(op.param1,Bots)
                        ke.acceptGroupInvitation(op.param1)
                        k7.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            k7.kickoutFromGroup(op.param1,[op.param2])
                            k7.inviteIntoGroup(op.param1,Bots)
                            ke.acceptGroupInvitation(op.param1)
                            ka.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.inviteIntoGroup(op.param1,Bots)
                                ke.acceptGroupInvitation(op.param1)
                                kb.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,Bots)
                                    ke.acceptGroupInvitation(op.param1)
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,Bots)
                                        ke.acceptGroupInvitation(op.param1)
                                        kd.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.inviteIntoGroup(op.param1,Bots)
                                            ke.acceptGroupInvitation(op.param1)
                                            kf.cancelGroupInvitation(op.param1,[op.param2])                     
                                        except:
                                            try:
                                                random.choice(team7).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team7).inviteIntoGroup(op.param1,Bots)
                                                ke.acceptGroupInvitation(op.param1)
                                                random.choice(team7).cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                random.choice(team7).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team7).inviteIntoGroup(op.param1,Bots)
                                                ke.acceptGroupInvitation(op.param1)
                                                random.choice(team7).cancelGroupInvitation(op.param1,[op.param2])
                else:pass
                return
            if Fmid in op.param3:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        k7.kickoutFromGroup(op.param1,[op.param2])
                        k7.inviteIntoGroup(op.param1,Bots)
                        kf.acceptGroupInvitation(op.param1)
                        ka.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,Bots)
                            kf.acceptGroupInvitation(op.param1)
                            kb.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,Bots)
                                kf.acceptGroupInvitation(op.param1)
                                kc.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,Bots)
                                    kf.acceptGroupInvitation(op.param1)
                                    kd.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,Bots)
                                        kf.acceptGroupInvitation(op.param1)
                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,Bots)
                                            kf.acceptGroupInvitation(op.param1)
                                            k7.cancelGroupInvitation(op.param1,[op.param2])                     
                                        except:
                                            try:
                                                random.choice(team8).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team8).inviteIntoGroup(op.param1,Bots)
                                                kf.acceptGroupInvitation(op.param1)
                                                random.choice(team8).cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                random.choice(team8).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team8).inviteIntoGroup(op.param1,Bots)
                                                kf.acceptGroupInvitation(op.param1)
                                                random.choice(team8).cancelGroupInvitation(op.param1,[op.param2])
                else:pass
                return
            if K7mid in op.param3:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,Bots)
                        k7.acceptGroupInvitation(op.param1)
                        kb.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,Bots)
                            k7.acceptGroupInvitation(op.param1)
                            kc.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,Bots)
                                k7.acceptGroupInvitation(op.param1)
                                kd.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,Bots)
                                    k7.acceptGroupInvitation(op.param1)
                                    ke.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,Bots)
                                        k7.acceptGroupInvitation(op.param1)
                                        kf.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.inviteIntoGroup(op.param1,Bots)
                                            k7.acceptGroupInvitation(op.param1)
                                            ka.cancelGroupInvitation(op.param1,[op.param2])                     
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.inviteIntoGroup(op.param1,Bots)
                                                k7.acceptGroupInvitation(op.param1)
                                                random.choice(team1).cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                random.choice(team1).kickoutFromGroup(op.param1,[op.param2])
                                                random.choice(team1).inviteIntoGroup(op.param1,Bots)
                                                k7.acceptGroupInvitation(op.param1)
                                                random.choice(team1).cancelGroupInvitation(op.param1,[op.param2])
                else:pass
                return
            if op.type == 19:
                if op.param3 in DZbot["Bots"]:
                    if op.param2 not in TEAM or op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3,Bots])
                            kb.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3,Bots])
                                kc.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3,Bots])
                                    kd.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3,Bots])
                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3,Bots])
                                            kf.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3,Bots])
                                                k7.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                                    k7.inviteIntoGroup(op.param1,[op.param3,Bots])
                                                    ka.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                        random.choice(team2).inviteIntoGroup(op.param1,[op.param3])
                                                        random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        random.choice(team2).inviteIntoGroup(op.param1,Bots)
                                                        random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                        random.choice(team2).cancelGroupInvitation(op.param1,[op.param2])
                    else:pass
                    return
                if op.param3 in ownerbot:
                    if op.param2 not in TEAM:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.findAndAddContactsByMid(op.param3)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.findAndAddContactsByMid(op.param3)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    X = random.choice(team2).getGroup(op.param1)
                                    X.preventedJoinByTicket = False
                                    random.choice(team2).updateGroup(X)
                                    Ticket = random.choice(team2).reissueGroupTicket(op.param1)
                                    time.sleep(0.001)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    k7.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            ke.findAndAddContactsByMid(op.param3)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kf.findAndAddContactsByMid(op.param3)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    k7.findAndAddContactsByMid(op.param3)
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                                    k7.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    try:
                                                        random.choice(team2).inviteIntoGroup(op.param1,[op.param3])
                                                        random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        random.choice(team2).inviteIntoGroup(op.param1,[op.param3])
                                                        random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                    else:pass
                    return
                if op.param3 in DZbot["admin"]:
                    if op.param2 not in TEAM or op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        wait["blacklist"][op.param2] = True
                        try:
                            ka.findAndAddContactsByMid(op.param3)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.findAndAddContactsByMid(op.param3)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            ke.findAndAddContactsByMid(op.param3)
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kf.findAndAddContactsByMid(op.param3)
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    k7.findAndAddContactsByMid(op.param3)
                                                    k7.kickoutFromGroup(op.param1,[op.param2])
                                                    k7.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    try:
                                                        random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                        random.choice(team2).inviteIntoGroup(op.param1,[op.param3])
                                                    except:
                                                        random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                        random.choice(team2).inviteIntoGroup(op.param1,[op.param3])
                    else:pass
                    return
        if op.type == 0:
            return
        if op.type == 5:
            if DZwait["autoAdd"] == True:
                if op.param2 not in TEAM:
                    cl.findAndAddContactsByMid(op.param1)
                    if (DZwait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, DZwait["message"])
        if op.type == 13:
            if mid in op.param3:
                if DZwait["autoJoin"] == True:
                    if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        cl.acceptGroupInvitation(op.param1)
                        anu = cl.getContact(op.param2)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in wait["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[_mid])
        if op.type == 13:
            if mid in op.param3:
                if DZwait["autoJoin"] == True:
                    if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        ka.acceptGroupInvitation(op.param1)
                        anu = ka.getContact(op.param2)
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        group = ka.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in wait["blacklist"]:
                            ka.kickoutFromGroup(op.param1,[_mid])
        if op.type == 13:
              if Bmid in op.param3:
                if DZwait["autoJoin"] == True:
                    if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        kb.acceptGroupInvitation(op.param1)
                        anu = kb.getContact(op.param2)
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        group = kb.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in wait["blacklist"]:
                            kb.kickoutFromGroup(op.param1,[_mid])
        if op.type == 13:
              if Cmid in op.param3:
                if DZwait["autoJoin"] == True:
                    if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        kc.acceptGroupInvitation(op.param1)
                        anu = kc.getContact(op.param2)
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        group = kc.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in wait["blacklist"]:
                            kc.kickoutFromGroup(op.param1,[_mid])
        if op.type == 13:
            if Dmid in op.param3:
                if DZwait["autoJoin"] == True:
                    if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        kd.acceptGroupInvitation(op.param1)
                        anu = kd.getContact(op.param2)
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        group = kd.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in wait["blacklist"]:
                            kd.kickoutFromGroup(op.param1,[_mid])
        if op.type == 13:
            if Emid in op.param3:
                if DZwait["autoJoin"] == True:
                    if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        ke.acceptGroupInvitation(op.param1)
                        anu = ke.getContact(op.param2)
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        group = ke.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in wait["blacklist"]:
                            ke.kickoutFromGroup(op.param1,[_mid])                            
        if op.type == 13:
            if Fmid in op.param3:
                if DZwait["autoJoin"] == True:
                    if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        kf.acceptGroupInvitation(op.param1)
                        anu = kf.getContact(op.param2)
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        group = kf.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in wait["blacklist"]:
                            kf.kickoutFromGroup(op.param1,[_mid])
        if op.type == 13:
            if K7mid in op.param3:
                if DZwait["autoJoin"] == True:
                    if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                        k7.acceptGroupInvitation(op.param1)
                        anu = k7.getContact(op.param2)
                        k7.leaveGroup(op.param1)
                    else:
                        k7.acceptGroupInvitation(op.param1)
                        group = k7.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in wait["blacklist"]:
                            k7.kickoutFromGroup(op.param1,[_mid])
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 in TEAM or op.param2 in DZbot["Bots"] or op.param2 in DZbot["admin"]:
                    pass
                else:
                    try:
                        if op.param3 in TEAM or op.param3 in DZbot["Bots"] or op.param3 in DZbot["admin"]:
                            pass
                        else:
                            if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                                wait["blacklist"][op.param2] = True
                                anu = cl.getCompactGroup(op.param1)
                                if anu.invitee is not None:
                                    pipo = [a.mid for a in anu.invitee]
                                    for target in pipo:
                                      if target in op.param3 and target not in TEAM and target not in DZbot["Bots"] and target not in DZbot["admin"]:
                                        wait["blacklist"][target] = True
                                        random.choice(team2).cancelGroupInvitation(op.param1,[target])
                                        random.choice(team2).kickoutFromGroup(op.param1,[target])
                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                            else:pass
                    except:
                        pass
            else:
                if op.param3 in TEAM or op.param3 in DZbot["Bots"] or op.param3 in DZbot["admin"]:pass
                else:
                    inv1 = op.param3.replace('\x1e',',')
                    inv2 = inv1.split(',')
                    for i in inv2:
                      if i in wait["blacklist"]:
                        try:
                            ka.cancelGroupInvitation(op.param1,[i])
                        except:
                            try:
                                kb.cancelGroupInvitation(op.param1,[i])
                            except:
                                try:
                                    kc.cancelGroupInvitation(op.param1,[i])
                                except:
                                    try:
                                        kd.cancelGroupInvitation(op.param1,[i])
                                    except:
                                        try:
                                            ke.cancelGroupInvitation(op.param1,[i])
                                        except:
                                            try:
                                                kf.cancelGroupInvitation(op.param1,[i])
                                            except:
                                                try:
                                                    k7.cancelGroupInvitation(op.param1,[i])
                                                except:
                                                    try:
                                                        random.choice(team2).cancelGroupInvitation(op.param1,[i])
                                                    except:
                                                        random.choice(team2).cancelGroupInvitation(op.param1,[i])
                        try:
                            random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                if op.param2 not in wait["blacklist"]:pass
                else:
                    inv1 = op.param3.replace('\x1e',',')
                    inv2 = inv1.split(',')
                    for i in inv2:
                        wait["blacklist"][i] = True
                        try:
                            ka.cancelGroupInvitation(op.param1,[i])
                        except:
                            try:
                                kb.cancelGroupInvitation(op.param1,[i])
                            except:
                                try:
                                    kc.cancelGroupInvitation(op.param1,[i])
                                except:
                                    try:
                                        kd.cancelGroupInvitation(op.param1,[i])
                                    except:
                                        try:
                                            ke.cancelGroupInvitation(op.param1,[i])
                                        except:
                                            try:
                                                kf.cancelGroupInvitation(op.param1,[i])
                                            except:
                                                try:
                                                    k7.cancelGroupInvitation(op.param1,[i])
                                                except:
                                                    try:
                                                        random.choice(team2).cancelGroupInvitation(op.param1,[i])
                                                    except:
                                                        random.choice(team2).cancelGroupInvitation(op.param1,[i])
        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass                                                                    
        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 in TEAM or op.param2 in DZbot["Bots"] or op.param2 in DZbot["admin"]:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                    try:
                        if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                            wait["blacklist"][op.param2] = True
                            if op.param3 not in wait["blacklist"]:
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kc.findAndAddContactsByMid(op.param3)
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kd.findAndAddContactsByMid(op.param3)
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    ke.findAndAddContactsByMid(op.param3)
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    pass
                            else:pass
                        else:pass
                    except:
                        pass
                        
        if op.type == 32:
            if op.param3 in JSmid:
#              if op.param3 in Bots:   
                if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.findAndAddContactsByMid(op.param3)
                            ka.inviteIntoGroup(op.param1,[JSmid])
                            ka.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                            ka.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)									
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.findAndAddContactsByMid(op.param3)
                                kb.inviteIntoGroup(op.param1,[JSmid])
                                kb.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                kb.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)										
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.inviteIntoGroup(op.param1,[JSmid])
                                    kc.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                    kc.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)										
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.inviteIntoGroup(op.param1,[JSmid])
                                        kd.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                        kd.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)											
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.findAndAddContactsByMid(op.param3)
                                            ke.inviteIntoGroup(op.param1,[JSmid])
                                            ke.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                            ke.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.findAndAddContactsByMid(op.param3)
                                                kf.inviteIntoGroup(op.param1,[JSmid])
                                                kf.sendMessage(op.param1,"Heh Maen cancel cipok ni 🙍")
                                                kf.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)			
                                        except:
                                            pass                   
                return                     
        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 in TEAM or op.param2 in DZbot["Bots"] or op.param2 in DZbot["admin"]:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                k7.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])
                    try:
                        if op.param2 not in TEAM and op.param2 not in DZbot["Bots"] and op.param2 not in DZbot["admin"]:
                            wait["blacklist"][op.param2] = True
                            if op.param3 not in wait["blacklist"]:
                                try:
                                    ka.findAndAddContactsByMid(op.param3)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kb.findAndAddContactsByMid(op.param3)
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kc.findAndAddContactsByMid(op.param3)
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                kd.findAndAddContactsByMid(op.param3)
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    ke.findAndAddContactsByMid(op.param3)
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    pass
                            else:pass
                        else:pass
                    except:
                        pass
        if op.type == 55:
            try:
                if op.param1 in DZwait["readPoint"]:
                   if op.param2 in DZwait["readMember"][op.param1]:
                       pass
                   else:
                       DZwait["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:        
            if op.param2 in wait["blacklist"]:
                if op.param2 not in TEAM and op.param2 not in DZbot["admin"] and op.param2 not in DZbot["Bots"]:
                    random.choice(team2).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if DZwait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"  💞 Check Sticker 💞\n💞 STKID : " + msg.contentMetadata["STKID"] +"\n💞 STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n💞 STKVER : " + msg.contentMetadata["STKVER"] + "\n💞 " + "line://shop/detail/" + msg.contentMetadata["STKPKGID"] +"")
               if msg.contentType == 13:
                 if DZwait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"💞 Nama : " + msg.contentMetadata["displayName"] + "\n💞 Mid : " + msg.contentMetadata["mid"] + "\n💞 Status : " + contact.statusMessage + "\n💞 Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "")
                        cl.sendImageWithURL(msg.to, image)  
 
               if msg.contentType == 13:
                 if msg._from in ownerbot:
                  if DZwait["abots"] == True:
                    if msg.contentMetadata["mid"] in DZbot["Bots"]:
                        cl.sendMessage(msg.to,"was bot friend")
                    else:
                        DZbot["Bots"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('DZbot.json','w','utf-8')
                        json.dump(DZbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add bots")
                 if DZwait["dbots"] == True:
                    if msg.contentMetadata["mid"] in DZbot["Bots"]:
                        del DZbot["Bots"][msg.contentMetadata["mid"]]
                        f=codecs.open('DZbot.json','w','utf-8')
                        json.dump(DZbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove bots")
                    else:
                        cl.sendMessage(msg.to,"Contact not in list bots")

                 if msg._from in ownerbot:
                  if DZwait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in DZbot["admin"]:
                        cl.sendMessage(msg.to,"was admin")
                    else:
                        DZbot["admin"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('DZbot.json','w','utf-8')
                        json.dump(DZbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add admin")
                 if DZwait["deladmin"] == True:
                    if msg.contentMetadata["mid"] in DZbot["admin"]:
                        del DZbot["admin"][msg.contentMetadata["mid"]]
                        f=codecs.open('DZbot.json','w','utf-8')
                        json.dump(DZbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove admin")
                    else:
                        cl.sendMessage(msg.to,"Contact not in list admin")

                 if msg._from in ownerbot:
                  if DZwait["ablacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"was blacklist")
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        cl.sendMessage(msg.to,"succes add in blacklist")
                 if DZwait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes remove blacklist")
                    else:
                        cl.sendMessage(msg.to,"Contact not in blacklist")

               if msg.contentType == 1:
                 if msg._from in ownerbot:
                    if DZwait["Aimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % DZwait["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Succses")
                        DZwait["Img"] = {}
                        DZwait["Aimage"] = False

               if msg.toType == 2:
                 if msg._from in ownerbot:
                   if settings["groupgambar"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupgambar"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Succes")

               if msg.contentType == 1:
                   if msg._from in ownerbot:
                       if mid in DZwait["foto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del DZwait["foto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Succes")

               if msg.contentType == 1:
                 if msg._from in ownerbot:
                        if Amid in DZwait["foto"]:
                            path = ka.downloadObjectMsg(msg_id)
                            del DZwait["foto"][Amid]
                            ka.updateProfilePicture(path1)
                            ka.sendMessage(msg.to,"Succes")
                        elif Bmid in DZwait["foto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del DZwait["foto"][Bmid]
                            kb.updateProfilePicture(path2)
                            kb.sendMessage(msg.to,"Succes")
                        elif Cmid in DZwait["foto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del DZwait["foto"][Cmid]
                            kc.updateProfilePicture(path3)
                            kc.sendMessage(msg.to,"Succes")
                        if Dmid in DZwait["foto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del DZwait["foto"][Dmid]
                            kd.updateProfilePicture(path4)
                            kd.sendMessage(msg.to,"Succes")
                        if Emid in DZwait["foto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del DZwait["foto"][Emid]
                            ke.updateProfilePicture(path5)
                            ke.sendMessage(msg.to,"Succes")
                        elif Fmid in DZwait["foto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del DZwait["foto"][Fmid]
                            kf.updateProfilePicture(path6)
                            kf.sendMessage(msg.to,"Succes")
                        elif K7mid in DZwait["foto"]:
                            path = k7.downloadObjectMsg(msg_id)
                            del DZwait["foto"][Fmid]
                            k7.updateProfilePicture(path7)
                            k7.sendMessage(msg.to,"Succes")

               if msg.contentType == 1:
                 if msg._from in ownerbot:
                   if settings["changegambar"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     path1 = ka.downloadObjectMsg(msg_id)
                     path2 = kb.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kd.downloadObjectMsg(msg_id)
                     path5 = ke.downloadObjectMsg(msg_id)
                     path6 = kf.downloadObjectMsg(msg_id)
                     path7 = k7.downloadObjectMsg(msg_id)
                     settings["changegambar"] = False
                     cl.updateProfilePicture(path1)
                     cl.sendMessage(msg.to, "Succes Ubah pic 0")
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to, "Succes Ubah pic 1")
                     kb.updateProfilePicture(path2)
                     kb.sendMessage(msg.to, "Succes Ubah pic 2")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Succes Ubab pic 3")
                     kd.updateProfilePicture(path4)
                     kd.sendMessage(msg.to, "Succes Ubah pic 4")
                     ke.updateProfilePicture(path5)
                     ke.sendMessage(msg.to, "Succes Ubah pic 5")
                     kf.updateProfilePicture(path6)
                     kf.sendMessage(msg.to, "Succes Ubah pic 6")
                     k7.updateProfilePicture(path7)
                     k7.sendMessage(msg.to, "Succes Ubah pic 7")

               if msg.contentType == 0:
                    if DZwait["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)                     
                        if cmd == "on":
                            if msg._from in ownerbot:
                                DZwait["selfbot"] = True
                                cl.sendMessage(msg.to, "Self bot mode on")

                        elif cmd == "off":
                            if msg._from in ownerbot:
                                DZwait["selfbot"] = False
                                cl.sendMessage(msg.to, "Self bot mode off")

                        elif cmd == "mod on":
                            if msg._from in ownerbot:
                                DZwait["talkban"] = True
                                cl.sendMessage(msg.to, "mode on in group")

                        elif cmd == "mod off":
                            if msg._from in ownerbot:
                                DZwait["talkban"] = False
                                cl.sendMessage(msg.to, "mode off in group")

                        elif cmd == "autojoin on" or text.lower() == 'join on':
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                DZwait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin allredy on")

                        elif cmd == "autojoin off" or text.lower() == 'join off':
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                DZwait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin allready off")
                          
                        elif cmd == "ออน":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               eltime = time.time() - listTimeLiking
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                               
                        elif cmd == "set":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                md = ""
                                if msg.to in protectqr: md+="Protect qr : on\n"
                                else: md+="Protect qr : off\n"   
                                if msg.to in protectjoin: md+="Protect join : on\n"
                                else: md+="Protect join : off\n"
                                if msg.to in protectkick: md+="Protect kick : on\n"
                                else: md+="Protect kick : off\n"
                                if msg.to in protectcancel: md+="Protect cancel : on\n"
                                else: md+="Protect cancel : off\n"
                                if msg.to in protectinvite: md+="Protect invite : on\n"
                                else: md+="Protect invite : off\n\n••Setings  protect••"                   
                                cl.sendMessage(msg.to, md)
                                
                        elif cmd == "help":
                            if msg._from in ownerbot:
                               helpMessage2 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage2))

                        elif text.lower() == "ลบแชท":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Berhasil bersihkan semua pesan ")
                               except:
                                   pass

                        elif text.lower() == "ลบแชทคิก":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Bersih ")
                                   ka.removeAllMessages(op.param2)
                                   ka.sendMessage(msg.to,"Bersih ")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to,"Bersih ")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"Bersih ")
                                   kd.removeAllMessages(op.param2)
                                   kd.sendMessage(msg.to,"Bersih ")
                                   ke.removeAllMessages(op.param2)
                                   ke.sendMessage(msg.to,"Bersih ")
                                   kf.removeAllMessages(op.param2)
                                   kf.sendMessage(msg.to,"Bersih ")
                                   k7.removeAllMessages(op.param2)
                                   k7.sendMessage(msg.to,"Bersih ")
                               except:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Bersih ")
                                   ka.removeAllMessages(op.param2)
                                   ka.sendMessage(msg.to,"Bersih ")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to,"Bersih ")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"Bersih ")
                                   kd.removeAllMessages(op.param2)
                                   kd.sendMessage(msg.to,"Bersih ")
                                   ke.removeAllMessages(op.param2)
                                   ke.sendMessage(msg.to,"Bersih ")
                                   kf.removeAllMessages(op.param2)
                                   kf.sendMessage(msg.to,"Bersih ")
                                   k7.removeAllMessages(op.param2)
                                   k7.sendMessage(msg.to,"Bersih ")
                        elif cmd == 'mid':
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                              cl.sendMessage(msg.to,mid+'","'+Amid+'","'+Bmid+'","'+Cmid+'","'+Dmid+'","'+Emid+'","'+Fmid)
                        elif cmd == "token":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               cl.sendMessage(msg.to,"threading.Thread(target=login, args=('a','"+ka.authToken+"')).start()")
                               ka.sendMessage(msg.to,"threading.Thread(target=login, args=('a','"+ka.authToken+"')).start()")
                               kb.sendMessage(msg.to,"threading.Thread(target=login, args=('b','"+kb.authToken+"')).start()")
                               kc.sendMessage(msg.to,"threading.Thread(target=login, args=('c','"+kc.authToken+"')).start()")
                               kd.sendMessage(msg.to,"threading.Thread(target=login, args=('d','"+kd.authToken+"')).start()")
                               ke.sendMessage(msg.to,"threading.Thread(target=login, args=('e','"+ke.authToken+"')).start()")
                               kf.sendMessage(msg.to,"threading.Thread(target=login, args=('f','"+kf.authToken+"')).start()")
                               k7.sendMessage(msg.to,"threading.Thread(target=login, args=('f','"+kf.authToken+"')).start()")
                        elif cmd == "speedbot" or cmd == "spb":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               start = time.time()
                               cl.sendMessage(msg.to, "สปีด")
                               elapsed_time = time.time() - start
                               ka.sendMessage(msg.to, "Speed\n{}".format(elapsed_time))
                               kb.sendMessage(msg.to, "Speed\n{}".format(elapsed_time))
                               kc.sendMessage(msg.to, "Speed\n{}".format(elapsed_time))
                               kd.sendMessage(msg.to, "Speed\n{}".format(elapsed_time))
                               ke.sendMessage(msg.to, "Speed\n{}".format(elapsed_time))
                               kf.sendMessage(msg.to, "Speed\n{}".format(elapsed_time))
                               k7.sendMessage(msg.to, "Speed\n{}".format(elapsed_time))
                        elif cmd == "speed" or cmd == "sp":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               start = time.time()
                               cl.sendMessage(msg.to, "สปีด")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "Speed\n{}".format(elapsed_time))
                               
                        elif cmd == "รี":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               cl.sendMessage(msg.to, "Proses rebooting.....")
                               DZwait["rePoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Berhasil reboot all bots")                   
#======================= Update Foto bots ====================#
                        elif cmd == "upg":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                              if msg.toType == 2:
                                settings["groupgambar"] = True
                                cl.sendMessage(msg.to,"Silahkan Kirim fotonya")

                        elif cmd == "up":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                settings["changegambar"] = True
                                cl.sendMessage(msg.to,"Silahkan kirim fotonya")

                        elif cmd == "1up":
                            if msg._from in ownerbot:
                                DZwait["foto"][Amid] = True
                                ka.sendMessage(msg.to,"Silahkan kirim foto nya")

                        elif cmd == "2up":
                            if msg._from in ownerbot:
                                DZwait["foto"][Bmid] = True
                                kb.sendMessage(msg.to,"Silahkan kirim foto nya")

                        elif cmd == "3up":
                            if msg._from in ownerbot:
                                DZwait["foto"][Cmid] = True
                                kc.sendMessage(msg.to,"Silahkan kirim foto nya")

                        elif cmd == "4up":
                            if msg._from in ownerbot:
                                DZwait["foto"][Dmid] = True
                                kd.sendMessage(msg.to,"Silahkan kirim foto nya")

                        elif cmd == "5up":
                            if msg._from in ownerbot:
                                DZwait["foto"][Emid] = True
                                ke.sendMessage(msg.to,"Silahkan kirim foto nya")
                                
                        elif cmd == "6up":
                            if msg._from in ownerbot:
                                DZwait["foto"][Fmid] = True
                                kf.sendMessage(msg.to,"Silahkan kirim foto nya")

                        elif cmd == "7up":
                            if msg._from in ownerbot:
                                DZwait["foto"][Fmid] = True
                                k7.sendMessage(msg.to,"Silahkan kirim foto nya")

                        elif cmd == "เปิดลิ้ง":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "ปิดลิ้ง":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "ลิ้ง":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
#======================= Update Name bots ====================#
                        elif cmd.startswith("me: "):
                          if msg._from in ownerbot:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("1me: "):
                          if msg._from in ownerbot:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ka.getProfile()
                                profile.displayName = string
                                ka.updateProfile(profile)
                                ka.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("2me: "):
                          if msg._from in ownerbot:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("3me: "):
                          if msg._from in ownerbot:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("4me: "):
                          if msg._from in ownerbot:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("5me: "):
                          if msg._from in ownerbot:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Succes " + string + "")
                                
                        elif cmd.startswith("6me: "):
                          if msg._from in ownerbot:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"Succes " + string + "") 

                        elif cmd.startswith("7me: "):
                          if msg._from in ownerbot:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k7.getProfile()
                                profile.displayName = string
                                k7.updateProfile(profile)
                                k7.sendMessage(msg.to,"Succes " + string + "") 

                        elif cmd == "มี":
                            if msg._from in ownerbot:
                              contact = cl.getContact(sender)
                              image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                              cl.sendMessage(msg.to, "Nama : "+str(contact.displayName))
                              cl.sendMessage(msg.to, None,contentMetadata={'mid': sender}, contentType=13)
                     
                        elif cmd == "bb":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                ka.sendMessage(msg.to,"พร้อม")
                                kb.sendMessage(msg.to,"พร้อม")
                                kc.sendMessage(msg.to,"พร้อม")
                                kd.sendMessage(msg.to,"พร้อม")
                                ke.sendMessage(msg.to,"พร้อม")
                                kf.sendMessage(msg.to,"พร้อม")
                                k7.sendMessage(msg.to,"พร้อม")


                        elif cmd == "iv":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                try:
                                    kicker = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,K7mid]
                                    cl.inviteIntoGroup(msg.to, kicker)
                                    ka.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    k7.acceptGroupInvitation(msg.to)
                                except:
                                    pass

                        elif cmd == "มา" or cmd == "in":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                k7.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k7.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k7.updateGroup(G)
                                kicker = [JSmid]
                                cl.inviteIntoGroup(msg.to, kicker)

                        elif cmd == "ออก" or cmd == "out":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                G = cl.getGroup(msg.to)
                                ka.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                k7.leaveGroup(msg.to)

                        elif cmd == "byeme":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "im sorry i leave in group "+str(G.name))
                                cl.leaveGroup(msg.to)
                      
                        elif 'Proqr ' in msg.text:
                           if msg._from in ownerbot:
                              spl = msg.text.replace('Proqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = ""
                                  cl.sendMessage(msg.to, "Protect url mode on in group")
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = ""
                                    else:
                                         msgs = ""
                                    cl.sendMessage(msg.to, "Protect url mode off in group")

                        elif 'Proinvite ' in msg.text:
                           if msg._from in ownerbot:
                              spl = msg.text.replace('Proinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Succes"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = ""
                                  cl.sendMessage(msg.to, "Protect invite mode on in group")
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = ""
                                    else:
                                         msgs = ""
                                    cl.sendMessage(msg.to, "Protect invite mode off in group")

                        elif 'Prokick ' in msg.text:
                           if msg._from in ownerbot:
                              spl = msg.text.replace('Prokick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Autokick on"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = ""
                                  cl.sendMessage(msg.to, "Protect kick mode on in group")
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = ""
                                    else:
                                         msgs = ""
                                    cl.sendMessage(msg.to, "Protect kick mode off in group")

                        elif 'Projoin ' in msg.text:
                           if msg._from in ownerbot:
                              spl = msg.text.replace('Projoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Projoin  on"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = ""
                                  cl.sendMessage(msg.to, "Protect join mode on in group")
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = ""
                                    else:
                                         msgs = ""
                                    cl.sendMessage(msg.to, "Protect join mode off in group")

                        elif 'Procancel ' in msg.text:
                           if msg._from in ownerbot:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Procancel on"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = ""
                                  cl.sendMessage(msg.to, "Protect cancel mode on in group")
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = ""
                                    else:
                                         msgs = ""
                                    cl.sendMessage(msg.to, "Protect cancel mode off in group")

                        elif 'Protect ' in msg.text:
                           if msg._from in ownerbot:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "mode on"
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = ""
                                  cl.sendMessage(msg.to,"All protect on in group")
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "mode off "
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = ""
                                    cl.sendMessage(msg.to, "All protect mode off")

                        elif ("มิด " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("ดึง " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass
                       
                        elif ("Bk " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in TEAM:
                                       try:
                                           random.choice(team2).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Bk2 " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in TEAM:
                                       try:
                                           kb.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Bk3 " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in TEAM:
                                       try:
                                           kc.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Bk4 " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in TEAM:
                                       try:
                                           kd.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Bk5 " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           ke.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Bk6 " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in TEAM:
                                       try:
                                           kf.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Bk7 " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in TEAM:
                                       try:
                                           k7.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Clcancelall" in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "Limit ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in TEAM and x not in DZbot["Bots"] and x not in DZbot ["admin"]:
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "Berhasil clear all")

                        elif ("Cancelall" in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "Limit ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in TEAM and x not in DZbot["Bots"] and x not in DZbot ["admin"]:
                                       random.choice(team2).cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "Clear all.")
                     
                        elif ("Addbot " in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           DZbot["Bots"][target] = True
                                           f=codecs.open('DZbot.json','w','utf-8')
                                           json.dump(DZbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           cl.sendMessage(msg.to,"Berhasil menambhkan bots")
                                       except:
                                           pass
                     
                        elif ("Dellbot " in msg.text):
                            if msg._from in ownerbot:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in TEAM:
                                        try:
                                            del DZbot["Bots"][target]
                                            f=codecs.open('DZbot.json','w','utf-8')
                                            json.dump(DZbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            cl.sendMessage(msg.to,"Berhasil dellete all bots")
                                        except:
                                            pass

                        elif cmd == "botlist" or text.lower() == 'bot list':
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                              if DZbot["Bots"] == {}:
                                cl.sendMessage(to,"💞💞💞💞")
                              else:
                                  mc = "   •••LIST ALL BOTS•••"
                                  for mi_d in DZbot["Bots"]:
                                      mc += "\n• "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "\n   ••• TEAM BOT PROTECT •••")
                     
                        elif cmd == "clear bot" or text.lower() == 'clear bot':
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                              DZbot["Bots"] = {}
                              kicker = cl.getContacts(DZbot["Bots"])
                              mc = "%i Bots " % len(kicker)
                              cl.sendMessage(msg.to,"Berhasil bersihkan all bot " +mc)
                      
                        elif cmd == "fresh" or text.lower() == 'refresh':
                            if msg._from in ownerbot:
                                DZwait["addadmin"] = False
                                DZwait["deladmin"] = False
                                DZwait["abots"] = False
                                DZwait["dbots"] = False
                                DZwait["ablacklist"] = False
                                DZwait["dblacklist"] = False
                                DZwait["Tablacklist"] = False
                                DZwait["Tdblacklist"] = False
                                cl.sendMessage(msg.to,"Berhasil Refresh all command")
                       
                        elif cmd == "bc" or text.lower() == 'banlist':
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot or msg._from in DHENZA:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(to," Kosong bos")
                              else:
                                  mc = "   List blacklist "
                                  for mi_d in wait["blacklist"]:
                                      mc += "\n👉 "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "")
                      
                        elif cmd == "clearban" or text.lower() == 'cb':
                          if msg._from in ownerbot or msg._from in DHENZA:
                            if msg._from in ownerbot:
                              ang = cl.getContacts(wait["blacklist"])
                              mc = "%i Korban " % len(ang)
                              cl.sendMessage(msg.to,"blacklist " +mc)
                              wait["blacklist"] = {}
                              
                        elif cmd == "js in":
                          if msg._from in ownerbot or msg._from in DHENZA:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0
                               ticket = cl.reissueGroupTicket(to)
                               ajs.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               
                        elif cmd == "js out":
                            if msg._from in ownerbot or msg._from in DHENZA:
                                G = cl.getGroup(msg.to)
                                ajs.sendMessage(msg.to, "Kicker Out  In "+str(G.name))
                                ajs.leaveGroup(msg.to)
                                
                        elif cmd == "iv js":
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [JSmid])
                                    cl.sendMessage(msg.to,"Succes invite di"+str(ginfo.name)+" Siap Stay")
                                except:
                                    pass
                                
                        elif 'Js ' in msg.text:
                           if msg._from in ownerbot or msg._from in DHENZA:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Protect Antikicker sudah aktif"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ✔ ]\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「 Status Protect Anti Kicker 」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ ❌ ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect Anti Kicker sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「 Status Protect Antikicker 」\n" + msgs)
                                    
                        elif cmd == "ck js":
                            if msg._from in ownerbot or msg._from in DHENZA:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)                                
                                md = "│╔══[ mai ] \n"
                                if msg.to in protectantijs: md+="│╠══[  STATUS ON  ] ᴊs✔️\n"
                                else: md+="│╠══[ STATUS OFF ] ᴊs❌\n"
                                md+= "│╚══[ mai ]"
                                cl.sendMessage(msg.to, md+"\n│ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│ᴊᴀᴍ  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")   
                                
                        elif cmd == "รายชื่อกลุ่ม":
                        	if msg._from in ownerbot or msg._from in DHENZA:
                                 groups = cl.groups
                                 ret_ = "╭──[ Group List ]"
                                 no = 0 
                                 for gid in groups:
                                     group = cl.getGroup(gid)
                                     ret_ += "\n│ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                     no += 1
                                 ret_ += "\n╰──[ Total {} Groups ]".format(str(len(groups)))
                                 k = len(ret_)//10000
                                 for aa in range(k+1):
                                     cl.sendMessage(to,'{}'.format(ret_[aa*10000 : (aa+1)*10000]))
                                     
                        elif cmd == "leavegroup":
                            	if msg._from in ownerbot or msg._from in DHENZA:                         		
                             		gr = cl.getGroupIdsJoined()                                    
                             		for group in gr:
                            	  	 	cl.sendMessage(group, "Leave All group i'm sorry \nJika perlu silahkan add Creator kami 👌👇\nhttp://line.me/ti/p/~teambotprotect")                        		   	
                                           
                        elif cmd.startswith('ivme '):
                              if msg._from in ownerbot or msg._from in DHENZA:    
                               text = msg.text.split()
                               number = text[1]
                               if number.isdigit():
                                groups = cl.getGroupIdsJoined()
                                if int(number) < len(groups) and int(number) >= 0:
                                    groupid = groups[int(number)]
                                    group = cl.getGroup(groupid)
                                    target = sender
                                    try:
                                        cl.getGroup(groupid)
                                        cl.findAndAddContactsByMid(target)
                                        cl.inviteIntoGroup(groupid, [target])
                                        cl.sendMessage(msg.to,"Succes invite to " + str(group.name))
                                    except:
                                        cl.sendMessage(msg.to,"I no there baby")                                                                               
                        
                        elif cmd.startswith("idcontact "):
                        	if msg._from in ownerbot or msg._from in DHENZA:
                                   if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                                contact = cl.getContact(ls)
                                                mi_d = contact.mid
                                                cl.sendContact(msg.to, mi_d)
                                                
                        elif cmd.startswith("contact "):
                        	if msg._from in ownerbot or msg._from in DHENZA:
                                       sep = cmd.split(" ")
                                       asu = cmd.replace(sep[0] + " ","")
                                       try:
                                          cl.sendContact(to, asu)
                                       except:
                                          pass

                        
                        elif cmd == "ck":
                            if msg._from in ownerbot or msg._from in DHENZA:
                               try:ka.inviteIntoGroup(to, [Amid]);has = "OK"
                               except:has = "NOT"
                               try:ka.kickoutFromGroup(to, [Amid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               ka.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))                               
                               try:kb.inviteIntoGroup(to, [Bmid]);has = "OK"
                               except:has = "NOT"
                               try:kb.kickoutFromGroup(to, [Bmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               kb.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:kc.inviteIntoGroup(to, [Cmid]);has = "OK"
                               except:has = "NOT"
                               try:kc.kickoutFromGroup(to, [Cmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               kc.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:kd.inviteIntoGroup(to, [Dmid]);has = "OK"
                               except:has = "NOT"
                               try:kd.kickoutFromGroup(to, [Dmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               kd.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:ke.inviteIntoGroup(to, [Emid]);has = "OK"
                               except:has = "NOT"
                               try:ke.kickoutFromGroup(to, [Emid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               ke.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:kf.inviteIntoGroup(to, [Fmid]);has = "OK"
                               except:has = "NOT"
                               try:kf.kickoutFromGroup(to, [Fmid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               kf.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
                               try:k7.inviteIntoGroup(to, [K7mid]);has = "OK"
                               except:has = "NOT"
                               try:k7.kickoutFromGroup(to, [K7mid]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "⭕"
                               else:sil = "⛔"
                               if has1 == "OK":sil1 = "⭕"
                               else:sil1 = "⛔"
                               k7.sendMessage(to, "sᴛᴀᴛᴜs:\n\nᴋɪᴄᴋ : {} \nɪɴᴠɪᴛᴇ : {}".format(sil1,sil))
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "มุดแล้วค่ะ : %s" % str(group.name))
                                     group1 = cl.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = ka.findGroupByTicket(ticket_id)
                                     ka.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     ka.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = ka.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     kb.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = kb.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     kc.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = kc.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = kd.findGroupByTicket(ticket_id)
                                     kd.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     kd.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = kd.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = ke.findGroupByTicket(ticket_id)
                                     ke.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     ke.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = ke.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = kf.findGroupByTicket(ticket_id)
                                     kf.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     kf.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = kf.findGroupByTicket(ticket_id)
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = k7.findGroupByTicket(ticket_id)
                                     k7.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     k7.sendMessage(msg.to, "ดีค่มุดแล้วค่ะ.. : %s" % str(group.name))
                                     groupl = k7.findGroupByTicket(ticket_id)
#===========KICKALL VIA BOT============#
                        elif ("Bubar" in msg.text):
                          if DZwait["selfbot"] == True:
                            if msg._from in ownerbot:
                               if msg.toType == 2:
                                  group = cl.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  for x in nama:
                                      if x not in TEAM:
                                          if x not in DZbot["Bots"]:
                                              if x not in DZbot["admin"]:
                                                  try:
                                                      klist=[ka,kb,kc,kd,ke]
                                                      kicker=random.choice(klist)
                                                      kicker.kickoutFromGroup(msg.to,[x])
                                                  except:
                                                      print ("limit")

    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
