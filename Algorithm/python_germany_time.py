import datetime,json

ind = datetime.datetime.now()
print(ind.now())
# print(ind.utcnow())

file =open('./time.json','r')
data =file.read()

if data:
    data =json.loads(data)
file.close()
if data=='' or not data['difference']:
    ger =input("enter germany time (24-hour time format)")
    ger =ger.strip().split(":")
    if len(ger)!=2:
        print('error in input')
        exit(0)
    ger =list(map(int,ger))
    ger_ins =datetime.datetime.now()
    ger_ins =ger_ins.replace(hour=ger[0],minute=ger[-1])

    delta =ind-ger_ins #difference between time interval
    # print(delta)
    germany_time =datetime.datetime.now()-delta
    delta2 =delta.__str__()
    with open('time.json','w') as file:
        a=json.dumps({'difference':delta2,'data':[germany_time.strftime('%H:%M:%S'),]})
        file.write(a)
else:
    delta =data['difference']
    delta =datetime.datetime.strptime(delta,'%H:%M:%S.%f')
    delta =datetime.timedelta(hours=delta.hour,minutes=delta.minute,seconds=delta.second,microseconds=delta.microsecond)
    # print(delta)
    germany_time =datetime.datetime.now()-delta
    with open('time.json','w') as file:
        data['data'].append(germany_time.strftime('%H:%M:%S'))
        data =json.dumps(data)
        file.write(data)
    
    
    
    # delta =datetime.timedelta(delta)
    # json_data['counter']+=1
    
# store this delta in json file
# germany_time_zone =datetime.timezone(-delta,name="GEN")


# germany_time.replace(tzinfo=germany_time_zone)
# print(germany_time_zone)
# print(germany_time.strftime('%H:%M:%S'))





