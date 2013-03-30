"""
nitin2.kumar@one97.net
"""



"""
Pulls data from central servers
By default pulls the gziped files
Additional parameter for other types or list of files.
python obd_et.py <operator> <filenames/filepaths>
works for obd only
<nitin2.kumar@one97.net>
"""

#! /usr/bin/env python

import os
import sys
import pexpect
import commands

class et:
    """
    Class et used as a configuration file

    """
    def __init__(self):
        pass

    #case 1 for all and direct central server connectivity
    use_case={'aircel':'1',\
              'idea':'1',\
              'reliance':'1',\
              'uninor':'2',\
              'videocon':'2',\
              'mts':'2',\
              'bsnl':'2',\
              'tata':'3',\
              'airtel_north':'1',\
              'airtel_south':'1',\
              'airtel_iffco':'2',\
              'vodafone':'2',\
              'tata_arpu':'2',\
              'sm_globacom':'2',\
              'sm_idea':'2',\
              'sm_reliance':'1',\
              'sm_vodafone':'2',\
              'sm_uninor':'2',\
              'sm_airtel':'2',\
              'sm_docomo':'1',\
              'sm_aircel':'2',\
              'sm_mts':'2',\
              'sm_hfcl':'2',\
              'sm_videocon':'2',\
              'sm_idea_punjab':'2',\
              'sm_vodafone_startalk':'2',\
              'sm_airtel_bangladesh':'1',\
              'sm_docomo_newsportal':'3'}


    server_ip={'aircel':'58.68.109.190',\
               'idea':'112.110.32.185',\
               'reliance':'220.226.188.21',\
               'tata':'192.168.1.2',\
               'uninor':'10.64.4.152',\
               'videocon':'10.64.10.178',\
               'mts':'10.130.0.186',\
               'bsnl':'192.168.1.4',\
               'airtel_north':'10.2.96.184',\
               'airtel_south':'10.49.36.21',\
               'airtel_iffco':'10.91.3.152',\
               'vodafone':'10.215.9.13',\
               'tata_arpu':'192.168.1.2',\
               'sm_globacom':'10.105.96.12',\
               'sm_idea':'10.0.106.36',\
               'sm_reliance':'220.226.188.124',\
               'sm_vodafone':'10.43.252.32',\
               'sm_uninor':'10.64.4.156',\
               'sm_airtel':'10.2.96.197',\
               'sm_docomo':'10.0.3.234',\
               'sm_aircel':'10.182.13.72',\
               'sm_mts':'10.130.14.66',
               'sm_hfcl':'192.8.2.113',\
               'sm_videocon':'10.64.10.166',\
               'sm_idea_punjab':'10.183.240.32',\
               'sm_vodafone_startalk':'10.43.252.11',\
               'sm_airtel_bangladesh':'10.201.20.10',\
               'sm_docomo_newsportal':'10.124.94.172'}


    user_ip={'aircel':'aircel',\
             'idea':'idea',\
             'reliance':'reliance',\
             'tata':'tata',\
             'uninor':'uninor',\
             'videocon':'videocon',\
             'mts':'mts',\
             'bsnl':'bsnl',\
             'airtel_north':'airtel',\
             'airtel_south':'airtel',\
             'airtel_iffco':'airtel',\
             'vodafone':'vodafone',\
             'tata_arpu':'tata',\
             'sm_globacom':'globacom',\
             'sm_idea':'dwh',\
             'sm_reliance':'dwh',\
             'sm_vodafone':'vodafone',\
             'sm_uninor':'uninor',\
             'sm_airtel':'airtel',\
             'sm_docomo':'tata',\
             'sm_aircel':'dwh',\
             'sm_mts':'mts',\
             'sm_hfcl':'hfcl',\
             'sm_videocon':'videocon',\
             'sm_idea_punjab':'idea',\
             'sm_vodafone_startalk':'vodafone',\
             'sm_airtel_bangladesh':'airtel',\
             'sm_docomo_newsportal':'tata'}

    pass_ip={'aircel':'aircel@197',\
             'idea':'dwh@#791',\
             'reliance':'reliance@197',\
             'tata':'tata@197',\
             'uninor':'uninor@197',\
             'videocon':'videocon@197',\
             'mts':'mts@197',\
             'bsnl':'bsnl@197',\
             'airtel_north':'airtel@197',\
             'airtel_south':'airtel@197',\
             'airtel_iffco':'airtel@197',\
             'vodafone':'vodafone@197',\
             'tata_arpu':'tata@197',\
             'sm_globacom':'globacom@197',\
             'sm_idea':'dwh@197',\
             'sm_reliance':'dwh@197',\
             'sm_vodafone':'vodafone@197',\
             'sm_uninor':'uninor@197',\
             'sm_airtel':'airtel@197',\
             'sm_docomo':'tata@197',\
             'sm_aircel':'dwh@197',\
             'sm_mts':'mts@197',\
             'sm_hfcl':'hfcl@197',\
             'sm_videocon':'videocon@197',\
             'sm_idea_punjab':'idea@197',\
             'sm_vodafone_startalk':'vodafone@197',\
             'sm_airtel_bangladesh':'airtel@one97',\
             'sm_docomo_newsportal':'tata@197'}

    source_path={'aircel':'/backup/dw_obd_csv',\
                 'idea':'/mysql/dump2csv',\
                 'reliance':'/reliance_dump/oct',\
                 'tata':'/backup/tata/dum2csv',\
                 'uninor':'/bkp/dump2csv',\
                 'videocon':'/backup/dw_obd_csv',\
                 'mts':'/mysql/dwh_csv',\
                 'bsnl':'/backup/dw_obd_csv',\
                 'airtel_north':'/backup/dw_obd_csv',\
                 'airtel_south':'/backup/dw_obd_csv',\
                 'airtel_iffco':'/backup/dumpcsv',\
                 'vodafone':'/mysql/obd_sep_csv',\
                 'tata_arpu':'/mysql/dump2csv/',\
                 'sm_globacom':'/bkp/hadoop',\
                 'sm_idea':'/backup/hadoop',\
                 'sm_reliance':'/backup/hadoop',\
                 'sm_vodafone':'/home/hadoop',\
                 'sm_uninor':'/home/hadoop',\
                 'sm_airtel':'/home/dwh/hadoop',\
                 'sm_docomo':'/home/tata/hadoop',\
                 'sm_aircel':'/bkp/hadoop',\
                 'sm_mts':'/backup/hadoop',\
                 'sm_hfcl':'/backup/hadoop',\
                 'sm_videocon':'/backup/hadoop',\
                 'sm_idea_punjab':'backup/idea/hadoop',\
                 'sm_vodafone_startalk':'/home/dwh/hadoop',\
                 'sm_airtel_bangladesh':'/home/airtel/hadoop',\
                 'sm_docomo_newsportal':'/home/tata/hadoop'}

    dest_path={'aircel':'/backup/data/obd/aircel',\
               'idea':'/backup/data/obd/idea',\
               'reliance':'/backup/data/obd/reliance',\
               'tata':'/backup/data/obd/tata_docomo',\
               'uninor':'/backup/data/obd/uninor',\
               'videocon':'/backup/data/obd/videocon',\
               'mts':'/backup/data/obd/mts',\
               'bsnl':'/backup/data/obd/bsnl',\
               'airtel_north':'/backup/data/obd/airtel_north',\
               'airtel_south':'/backup/data/obd/airtel_south',\
               'airtel_iffco':'/backup/data/obd/airtel_iffco',\
               'vodafone':'/backup/data/obd/vodafone',\
               'tata_arpu':'/backup/data/arpu/tata',\
               'sm_globacom':'/backup/data/sm/fresh',\
               'sm_idea':'/backup/data/sm/fresh',\
               'sm_reliance':'/backup/data/sm/fresh',\
               'sm_vodafone':'/backup/data/sm/fresh',\
               'sm_uninor':'/backup/data/sm/fresh',\
               'sm_airtel':'/backup/data/sm/fresh',\
               'sm_docomo':'/backup/data/sm/fresh',\
               'sm_aircel':'/backup/data/sm/fresh',\
               'sm_mts':'/backup/data/sm/fresh',\
               'sm_hfcl':'/backup/data/sm/fresh',\
               'sm_videocon':'/backup/data/sm/fresh',\
               'sm_idea_punjab':'/backup/data/sm/fresh',\
               'sm_vodafone_startalk':'/backup/data/sm/fresh',\
               'sm_airtel_bangladesh':'/backup/data/sm/fresh',\
               'sm_docomo_newsportal':'/backup/data/sm/fresh'}

    #case 3 for two server gateways.
    sg_ip_one={'tata':'10.0.1.173',\
               'uninor':'10.64.4.148',\
               'videocon':'180.214.158.155',\
               'mts':'202.78.174.28',\
               'bsnl':'218.248.80.123',\
               'airtel_north':'117.99.128.51',\
               'airtel_south':'117.99.128.51',\
               'airtel_iffco':'59.145.145.211',\
               'vodafone':'203.199.126.79',\
               'tata_arpu':'10.0.1.173',\
               'sm_globacom':'41.203.65.178',\
               'sm_idea':'112.110.32.228',\
               'sm_reliance':'1',\
               'sm_vodafone':'210.210.26.35',\
               'sm_uninor':'10.64.4.148',\
               'sm_airtel':'10.2.96.184',\
               'sm_docomo':'2',\
               'sm_aircel':'202.148.206.78',\
               'sm_mts':'202.78.174.28',\
               'sm_hfcl':'202.164.33.238',\
               'sm_videocon':'180.214.158.155',\
               'sm_idea_punjab':'112.110.32.228',\
               'sm_vodafone_startalk':'210.210.26.35',\
               'sm_airtel_bangladesh':'2',\
               'sm_docomo_newsportal':'10.0.5.51'}

    sg_ip_two={'tata':'172.17.104.48',\
               'airtel_north':'10.2.29.67',\
               'airtel_south':'10.2.29.67',\
               'tata_arpu':'172.17.104.48',\
               'sm_docomo_newsportal':'172.31.201.13'}

    sg_un_one={'tata':'dwh',\
               'uninor':'unigate',\
               'videocon':'datacom',\
               'mts':'administrator',\
               'bsnl':'administrator',\
               'airtel_north':'administrator',\
               'airtel_south':'administrator',\
               'airtel_iffco':'root',\
               'vodafone':'pinkfloyd',\
               'tata_arpu':'dwh',\
               'sm_globacom':'globacom',\
               'sm_idea':'administrator',\
               'sm_reliance':'1',\
               'sm_vodafone':'vodafone',\
               'sm_uninor':'unigate',\
               'sm_airtel':'airtel',\
               'sm_docomo':'2',\
               'sm_aircel':'pinkfloyd',\
               'sm_mts':'administrator',\
               'sm_hfcl':'administrator',\
               'sm_videocon':'datacom',\
               'sm_idea_punjab':'administrator',\
               'sm_vodafone_startalk':'vodafone',\
               'sm_airtel_bangladesh':'2',\
               'sm_docomo_newsportal':'root'}

    sg_un_two={'tata':'tata',\
               'airtel_north':'puttyuser',\
               'airtel_south':'puttyuser',\
               'tata_arpu':'root',\
               'sm_docomo_newsportal':'tata'}

    sg_pass_one={'tata':'dwh@197',\
                 'uninor':'un1g@te@971',\
                 'videocon':'datacom@197',\
                 'mts':'mts@lockpicking',\
                 'bsnl':'f0rever0ne197',\
                 'airtel_north':'raj@one97',\
                 'airtel_south':'raj@one97',\
                 'airtel_iffco':'lockpicking',\
                 'vodafone':'Creativity',\
                 'tata_arpu':'dwh@197',\
                 'sm_globacom':'globacom@197',\
                 'sm_idea':'service@idea',\
                 'sm_reliance':'1',\
                 'sm_vodafone':'vodafone@197',\
                 'sm_uninor':'un1g@te@971',\
                 'sm_airtel':'lock@971',\
                 'sm_docomo':'2',\
                 'sm_aircel':'one97@aircel',\
                 'sm_mts':'mts@lockpicking',\
                 'sm_hfcl':'hfcl#pun%in',\
                 'sm_videocon':'datacom@197',\
                 'sm_idea_punjab':'service@idea',\
                 'sm_vodafone_startalk':'vodafone@197',\
                 'sm_airtel_bangladesh':'2',\
                 'sm_docomo_newsportal':'redhat'}

    sg_pass_two={'tata':'tata@197',\
                 'airtel_north':'secured!197',\
                 'airtel_south':'secured!197',\
                 'tata_arpu':'redhat',\
                 'sm_docomo_newsportal':'tata@197'}

    port_one={'tata':'7273',\
              'uninor':'5147',\
              'videocon':'5499',\
              'mts':'7427',\
              'bsnl':'8013',\
              'airtel_north':'2971',\
              'airtel_south':'2978',\
              'airtel_iffco':'3878',\
              'vodafone':'5789',\
              'tata_arpu':'1728',\
              'sm_globacom':'9612',\
              'sm_idea':'3622',\
              'sm_reliance':'1',\
              'sm_vodafone':'3222',\
              'sm_uninor':'5622',\
              'sm_airtel':'9722',\
              'sm_docomo':'2',\
              'sm_aircel':'7222',\
              'sm_mts':'6622',\
              'sm_hfcl':'11322',\
              'sm_videocon':'6622',\
              'sm_idea_punjab':'3222',\
              'sm_vodafone_startalk':'1122',\
              'sm_airtel_bangladesh':'2',\
              'sm_docomo_newsportal':'1322'}

    port_two={'tata':'6673',\
              'airtel_north':'6186',\
              'airtel_south':'3678',\
              'tata_arpu':'1729',\
              'sm_docomo_newsportal':'7222'}


    def get_filenames(self,fname):
        pass


def pull(myet,operator,filenames=['*.gz']):

    '''
    try:
        for root, dirs, files in os.walk(myet.dest_path[operator]):
           for name in files:
               print("Deleting file: %s"%(name))
               os.remove(os.path.join(root, name))
    except (Exception,e):
        print("%s does not exist!"%(myet.dest_path[operator]))
    '''

    if not os.path.exists(myet.dest_path[operator]):
        os.system("mkdir -p %s" %myet.dest_path[operator])
        print("Directory created %s" %myet.dest_path[operator])


    if myet.use_case[operator]=='1':

        display_details(myet,operator)

        for filename in filenames:
            try :
                print("scp -r %s@%s:%s/%s  %s" %(myet.user_ip[operator],myet.server_ip[operator],myet.source_path[operator],filename,myet.dest_path[operator]))
                foo5=pexpect.spawn("scp -r %s@%s:%s/%s  %s" %(myet.user_ip[operator],myet.server_ip[operator],myet.source_path[operator],filename,myet.dest_path[operator]))
                foo5.expect('.ssword:*')
                print("Sending password %s" %(myet.pass_ip[operator]))
                foo5.sendline("%s" %(myet.pass_ip[operator]))
                foo5.interact()
                foo5.close()
            except Exception,e:
                print("Exception for operator %s!" %myet.user_ip[operator])
                print(e)
            pass
    #case 2
    if myet.use_case[operator]=='2':
        #kill any active ports if any
        os.system("/sbin/fuser -k %s/tcp" %myet.port_one[operator])
        #display et details
        display_details(myet,operator)

        try :
            print("/usr/bin/ssh -o HostKeyAlias=%s -f -N -l %s -L %s:%s:22 %s" %(myet.sg_ip_one[operator],myet.sg_un_one[operator],myet.port_one[operator],myet.server_ip[operator],myet.sg_ip_one[operator]))
            foo9=pexpect.spawn("/usr/bin/ssh -o HostKeyAlias=%s -f -N -l %s -L %s:%s:22 %s" %(myet.sg_ip_one[operator],myet.sg_un_one[operator],myet.port_one[operator],myet.server_ip[operator],myet.sg_ip_one[operator]))
            foo9.expect('.ssword:*')
            print("Sending password %s" %myet.sg_pass_one[operator])
            foo9.sendline("%s" %myet.sg_pass_one[operator])
            #foo1.interact()
            foo9.close()
            print("Connection made to SG1 %s" %myet.sg_ip_one[operator])
        except Exception,e:
            print("Exception for operator %s first connection!" %operator)
            print (e)
            pass

        for filename in filenames:
            try :
                print("spawning")
                print("/usr/bin/scp -o HostKeyAlias=%s -P %s %s@localhost:%s/%s  %s" %(myet.server_ip[operator],myet.port_one[operator],myet.user_ip[operator],myet.source_path[operator],filename,myet.dest_path[operator]))
                foo8=pexpect.spawn("/usr/bin/scp -o HostKeyAlias=%s -P %s %s@localhost:%s/%s  %s" %(myet.server_ip[operator],myet.port_one[operator],myet.user_ip[operator],myet.source_path[operator],filename,myet.dest_path[operator]))
                foo8.expect('.ssword:*')
                print("sending password %s" %myet.pass_ip[operator])
                foo8.sendline("%s" %myet.pass_ip[operator])
                foo8.interact()
                foo8.close()
            except Exception,e:
                print("Exception for operator %s final scp!" %operator)
                print(e)
                pass

    #case 3
    if myet.use_case[operator]=='3':
        #kill active ports if any
        os.system("/sbin/fuser -k %s/tcp" %myet.port_one[operator])
        os.system("/sbin/fuser -k %s/tcp" %myet.port_two[operator])
        #display et details
        display_details(myet,operator)

        try :
            print("/usr/bin/ssh -o HostKeyAlias=%s -f -N -l %s -L %s:%s:22 %s" %(myet.sg_ip_one[operator],myet.sg_un_one[operator],myet.port_one[operator],myet.sg_ip_two[operator],myet.sg_ip_one[operator]))
            foo5=pexpect.spawn("/usr/bin/ssh -o HostKeyAlias=%s -f -N -l %s -L %s:%s:22 %s" %(myet.sg_ip_one[operator],myet.sg_un_one[operator],myet.port_one[operator],myet.sg_ip_two[operator],myet.sg_ip_one[operator]))
            foo5.expect('.ssword:*')
            print("Sending password %s" %myet.sg_pass_one[operator])
            foo5.sendline("%s\r\n" %myet.sg_pass_one[operator])
            foo5.sendline("\r\n")
            #foo5.interact()
            foo5.close()
            print("Connection made to SG1 %s" %myet.sg_ip_one[operator])
        except Exception,e:
            print("Exception for operator %s first connection!" %operator)
            print (e)
            pass
        try :
            print("/usr/bin/ssh -o HostKeyAlias=%s -p %s -f -N -l %s -L %s:%s:22 localhost" %(myet.sg_ip_two[operator],myet.port_one[operator],myet.sg_un_two[operator],myet.port_two[operator],myet.server_ip[operator]))
            foo6=pexpect.spawn("/usr/bin/ssh -o HostKeyAlias=%s -p %s -f -N -l %s -L %s:%s:22 localhost" %(myet.sg_ip_two[operator],myet.port_one[operator],myet.sg_un_two[operator],myet.port_two[operator],myet.server_ip[operator]))
            foo6.expect('.ssword:*')
            foo6.sendline("%s\r\n" %myet.sg_pass_two[operator])
            #foo6.interact()
            foo6.close()
            print("Connection made to SG2 %s" %myet.sg_ip_two[operator])
        except Exception,e:
            print("Exception for operator %s second connection!" %operator)
            print (e)
            pass

        for filename in filenames:
            try :
                print("/usr/bin/scp -o HostKeyAlias=%s -P %s %s@localhost:%s/%s  %s" %(myet.server_ip[operator],myet.port_two[operator],myet.user_ip[operator],myet.source_path[operator],filename,myet.dest_path[operator]))
                foo7=pexpect.spawn("/usr/bin/scp -o HostKeyAlias=%s -P %s %s@localhost:%s/%s %s" %(myet.server_ip[operator],myet.port_two[operator],myet.user_ip[operator],myet.source_path[operator],filename,myet.dest_path[operator]))
                foo7.expect('.ssword:*')
                print("Sending password %s" %myet.pass_ip[operator])
                foo7.sendline("%s\r\n" %myet.pass_ip[operator])
                #foo5.sendline("\r\n")
                foo7.interact()
                foo7.close()
            except Exception,e:
                print("Exception for operator %s final scp!" %operator)
                print(e)
                pass

def display_details(myet,operator):
    print("Operator : %s" %operator)
    print("Server IP : %s" %myet.server_ip[operator])
    print("Username : %s" %myet.user_ip[operator])
    print("Password : %s" %myet.pass_ip[operator])
    print("Source path : %s" %myet.source_path[operator])
    print("Destionation path : %s" %myet.dest_path[operator])


def printUsage():
    print('Usage: python obd_et.py <operator>')
    print('Usage: python obd_et.py <operator> <filename>')

def varifyOperator(operator):
    if operator in ('aircel','airtel','mts','uninor','reliance','idea','tata','tata_docomo','bsnl','videocon','vodafone',\
                    'airtel_north','airtel_south','airtel_iffco','tata_arpu','sm_idea','sm_globacom','sm_uninor',\
                    'sm_reliance','sm_airtel','sm_vodafone','sm_videocon','sm_hfcl','sm_idea_punjab','sm_vodafone_startalk','sm_airtel_bangladesh',\
                    'sm_docomo_newsportal'):
        return True
    else:
        return False

def main():

    if (len(sys.argv) == 1):
        printUsage()
        sys.exit(1)

    if (len(sys.argv) == 2):
        operator=sys.argv[1]
        if varifyOperator(sys.argv[1]):
            print (operator)
            myet=et()
            pull(myet,operator)
        else:
            print ("Unknown operator! %s" %(operator))
            printUsage()
            sys.exit(1)

    if (len(sys.argv) >= 3):
        operator=sys.argv[1]
        filenames=sys.argv[2:]
        if varifyOperator(sys.argv[1]):
            print (operator)
            myet=et()
            pull(myet,operator,filenames)

        else:
            print ("Unknown operator! %s" %(operator))
            printUsage()
            sys.exit(1)

if __name__=='__main__':
    main()



