#!/usr/bin/python

#languages list
langs = [
"all All languages",
"ara Arabic",
"aar Afar",
"abk Abkhazian",
"ace Achinese",
"ach Acoli",
"ada Adangme",
"ady adyghe",
"afa Afro-Asiatic",
"afh Afrihili",
"afr Afrikaans",
"ain Ainu",
"aka Akan",
"akk Akkadian",
"alb Albanian",
"ale Aleut",
"alg Algonquian",
"alt Southern",
"amh Amharic",
"ang English",
"apa Apache",
"arc Aramaic",
"arg Aragonese",
"arm Armenian",
"arn Araucanian",
"arp Arapaho",
"art Artificial",
"arw Arawak",
"asm Assamese",
"ast Asturian",
"ath Athapascan",
"aus Australian",
"ava Avaric",
"ave Avestan",
"awa Awadhi",
"aym Aymara",
"aze Azerbaijani",
"bad Banda",
"bai Bamileke",
"bak Bashkir",
"bal Baluchi",
"bam Bambara",
"ban Balinese",
"baq Basque",
"bas Basa",
"bat Baltic",
"bej Beja",
"bel Belarusian",
"bem Bemba",
"ben Bengali",
"ber Berber",
"bho Bhojpuri",
"bih Bihari",
"bik Bikol",
"bin Bini",
"bis Bislama",
"bla Siksika",
"bnt Bantu",
"bos Bosnian",
"bra Braj",
"bre Breton",
"btk Batak",
"bua Buriat",
"bug Buginese",
"bul Bulgarian",
"bur Burmese",
"byn Blin",
"cad Caddo",
"cai Central",
"car Carib",
"cat Catalan",
"cau Caucasian",
"ceb Cebuano",
"cel Celtic",
"cha Chamorro",
"chb Chibcha",
"che Chechen",
"chg Chagatai",
"chi Chinese",
"chk Chuukese",
"chm Mari",
"chn Chinook",
"cho Choctaw",
"chp Chipewyan",
"chr Cherokee",
"chu Church",
"chv Chuvash",
"chy Cheyenne",
"cmc Chamic",
"cop Coptic",
"cor Cornish",
"cos Corsican",
"cpe Creoles",
"cpf Creoles",
"cpp Creoles",
"cre Cree",
"crh Crimean",
"crp Creoles",
"csb Kashubian",
"cus Cushitic",
"cze Czech",
"dak Dakota",
"dan Danish",
"dar Dargwa",
"day Dayak",
"del Delaware",
"den Slave",
"dgr Dogrib",
"din Dinka",
"div Divehi",
"doi Dogri",
"dra Dravidian",
"dua Duala",
"dum Dutch",
"dut Dutch",
"dyu Dyula",
"dzo Dzongkha",
"efi Efik",
"egy Egyptian",
"eka Ekajuk",
"elx Elamite",
"eng English",
"enm English",
"epo Esperanto",
"est Estonian",
"ewe Ewe",
"ewo Ewondo",
"fan Fang",
"fao Faroese",
"fat Fanti",
"fij Fijian",
"fil Filipino",
"fin Finnish",
"fiu Finno-Ugrian",
"fon Fon",
"fre French",
"frm French",
"fro French",
"fry Frisian",
"ful Fulah",
"fur Friulian",
"gaa Ga",
"gay Gayo",
"gba Gbaya",
"gem Germanic",
"geo Georgian",
"ger German",
"gez Geez",
"gil Gilbertese",
"gla Gaelic",
"gle Irish",
"glg Galician",
"glv Manx",
"gmh German",
"goh German",
"gon Gondi",
"gor Gorontalo",
"got Gothic",
"grb Grebo",
"grc Greek",
"ell Greek",
"grn Guarani",
"guj Gujarati",
"gwi Gwichin",
"hai Haida",
"hat Haitian",
"hau Hausa",
"haw Hawaiian",
"heb Hebrew",
"her Herero",
"hil Hiligaynon",
"him Himachali",
"hin Hindi",
"hit Hittite",
"hmn Hmong",
"hmo Hiri",
"hrv Croatian",
"hun Hungarian",
"hup Hupa",
"iba Iban",
"ibo Igbo",
"ice Icelandic",
"ido Ido",
"iii Sichuan",
"ijo Ijo",
"iku Inuktitut",
"ile Interlingue",
"ilo Iloko",
"ina Interlingua",
"inc Indic",
"ind Indonesian",
"ine Indo-European",
"inh Ingush",
"ipk Inupiaq",
"ira Iranian",
"iro Iroquoian",
"ita Italian",
"jav Javanese",
"jpn Japanese",
"jpr Judeo-Persian",
"jrb Judeo-Arabic",
"kaa Kara-Kalpak",
"kab Kabyle",
"kac Kachin",
"kal Kalaallisut",
"kam Kamba",
"kan Kannada",
"kar Karen",
"kas Kashmiri",
"kau Kanuri",
"kaw Kawi",
"kaz Kazakh",
"kbd Kabardian",
"kha Khasi",
"khi Khoisan",
"khm Khmer",
"kho Khotanese",
"kik Kikuyu",
"kin Kinyarwanda",
"kir Kirghiz",
"kmb Kimbundu",
"kok Konkani",
"kom Komi",
"kon Kongo",
"kor Korean",
"kos Kosraean",
"kpe Kpelle",
"krc Karachay-Balkar",
"kro Kru",
"kru Kurukh",
"kua Kuanyama",
"kum Kumyk",
"kur Kurdish",
"kut Kutenai",
"lad Ladino",
"lah Lahnda",
"lam Lamba",
"lao Lao",
"lat Latin",
"lav Latvian",
"lez Lezghian",
"lim Limburgan",
"lin Lingala",
"lit Lithuanian",
"lol Mongo",
"loz Lozi",
"ltz Luxembourgish",
"lua Luba-Lulua",
"lub Luba-Katanga",
"lug Ganda",
"lui Luiseno",
"lun Lunda",
"luo Luo",
"lus lushai",
"mac Macedonian",
"mad Madurese",
"mag Magahi",
"mah Marshallese",
"mai Maithili",
"mak Makasar",
"mal Malayalam",
"man Mandingo",
"mao Maori",
"map Austronesian",
"mar Marathi",
"mas Masai",
"may Malay",
"mdf Moksha",
"mdr Mandar",
"men Mende",
"mga Irish",
"mic Mi'kmaq",
"min Minangkabau",
"mis Miscellaneous",
"mkh Mon-Khmer",
"mlg Malagasy",
"mlt Maltese",
"mnc Manchu",
"mni Manipuri",
"mno Manobo",
"moh Mohawk",
"mol Moldavian",
"mon Mongolian",
"mos Mossi",
"mwl Mirandese",
"mul Multiple",
"mun Munda",
"mus Creek",
"mwr Marwari",
"myn Mayan",
"myv Erzya",
"nah Nahuatl",
"nai North",
"nap Neapolitan",
"nau Nauru",
"nav Navajo",
"nbl Ndebele",
"nde Ndebele",
"ndo Ndonga",
"nds Low",
"nep Nepali",
"new Nepal",
"nia Nias",
"nic Niger-Kordofanian",
"niu Niuean",
"nno Norwegian",
"nob Norwegian",
"nog Nogai",
"non Norse",
"nor Norwegian",
"nso Northern",
"nub Nubian",
"nwc Classical",
"nya Chichewa",
"nym Nyamwezi",
"nyn Nyankole",
"nyo Nyoro",
"nzi Nzima",
"oci Occitan",
"oji Ojibwa",
"ori Oriya",
"orm Oromo",
"osa Osage",
"oss Ossetian",
"ota Turkish",
"oto Otomian",
"paa Papuan",
"pag Pangasinan",
"pal Pahlavi",
"pam Pampanga",
"pan Panjabi",
"pap Papiamento",
"pau Palauan",
"peo Persian",
"per Persian",
"phi Philippine",
"phn Phoenician",
"pli Pali",
"pol Polish",
"pon Pohnpeian",
"por Portuguese",
"pra Prakrit",
"pro Provencal",
"pus Pushto",
"que Quechua",
"raj Rajasthani",
"rap Rapanui",
"rar Rarotongan",
"roa Romance",
"roh Raeto-Romance",
"rom Romany",
"run Rundi",
"rup Aromanian",
"rus Russian",
"sad Sandawe",
"sag Sango",
"sah Yakut",
"sai South",
"sal Salishan",
"sam Samaritan",
"san Sanskrit",
"sas Sasak",
"sat Santali",
"scc Serbian",
"scn Sicilian",
"sco Scots",
"sel Selkup",
"sem Semitic",
"sga Irish",
"sgn Sign",
"shn Shan",
"sid Sidamo",
"sin Sinhalese",
"sio Siouan",
"sit Sino-Tibetan",
"sla Slavic",
"slo Slovak",
"slv Slovenian",
"sma Southern",
"sme Northern",
"smi Sami",
"smj Lule",
"smn Inari",
"smo Samoan",
"sms Skolt",
"sna Shona",
"snd Sindhi",
"snk Soninke",
"sog Sogdian",
"som Somali",
"son Songhai",
"sot Sotho",
"spa Spanish",
"srd Sardinian",
"srr Serer",
"ssa Nilo-Saharan",
"ssw Swati",
"suk Sukuma",
"sun Sundanese",
"sus Susu",
"sux Sumerian",
"swa Swahili",
"swe Swedish",
"syr Syriac",
"tah Tahitian",
"tai Tai",
"tam Tamil",
"tat Tatar",
"tel Telugu",
"tem Timne",
"ter Tereno",
"tet Tetum",
"tgk Tajik",
"tgl Tagalog",
"tha Thai",
"tib Tibetan",
"tig Tigre",
"tir Tigrinya",
"tiv Tiv",
"tkl Tokelau",
"tlh Klingon",
"tli Tlingit",
"tmh Tamashek",
"tog Tonga",
"ton Tonga",
"tpi Tok",
"tsi Tsimshian",
"tsn Tswana",
"tso Tsonga",
"tuk Turkmen",
"tum Tumbuka",
"tup Tupi",
"tur Turkish",
"tut Altaic",
"tvl Tuvalu",
"twi Twi",
"tyv Tuvinian",
"udm Udmurt",
"uga Ugaritic",
"uig Uighur",
"ukr Ukrainian",
"umb Umbundu",
"und Undetermined",
"urd Urdu",
"uzb Uzbek",
"vai Vai",
"ven Venda",
"vie Vietnamese",
"vol Volapuk",
"vot Votic",
"wak Wakashan",
"wal Walamo",
"war Waray",
"was Washo",
"wel Welsh",
"wen Sorbian",
"wln Walloon",
"wol Wolof",
"xal Kalmyk",
"xho Xhosa",
"yao Yao",
"yap Yapese",
"yid Yiddish",
"yor Yoruba",
"ypk Yupik",
"zap Zapotec",
"zen Zenaga",
"zha Zhuang",
"znd Zande",
"zul Zulu",
"zun Zuni",
"rum Romanian",
"pob Portuguese",
"mne Montenegrin",
"zht Chinese",
"zhe Chinese"]

import wx,os,struct,sys,urllib2,gzip
from xmlrpclib import ServerProxy, Error

#hash string generation
def hashFile(name): 
    try: 
        longlongformat = 'q' 
        bytesize = struct.calcsize(longlongformat)             
        f = open(name, "rb")            
        filesize = os.path.getsize(name) 
        hash = filesize            
        if filesize < 65536 * 2: 
               return "SizeError"         
        for x in range(65536/bytesize): 
                buffer = f.read(bytesize) 
                (l_value,)= struct.unpack(longlongformat, buffer)  
                hash += l_value 
                hash = hash & 0xFFFFFFFFFFFFFFFF 
        f.seek(max(0,filesize-65536),0) 
        for x in range(65536/bytesize): 
                buffer = f.read(bytesize) 
                (l_value,)= struct.unpack(longlongformat, buffer)  
                hash += l_value 
                hash = hash & 0xFFFFFFFFFFFFFFFF   
        f.close() 
        returnedhash =  "%016x" % hash 
        return returnedhash 
    except(IOError): 
        return "IOError" 

class Movie(wx.Frame):       
    def __init__(self):
        try:
            #gui setup
            wx.Frame.__init__(self, None, wx.ID_ANY)
            self.container = wx.StaticBox(self, label='Movie', pos=(5, 5), size=(790, 420))
            self.nameLb = wx.StaticText(self, -1, "Name:", pos=(25, 32))
            self.nameTb = wx.TextCtrl(self, -1, "", pos=(80, 30), size=(700, -1))
            self.imdbLb = wx.StaticText(self, -1, "IMDB:", pos=(25, 62))
            self.imdbTb = wx.TextCtrl(self, -1, "", pos=(80, 60), size=(700, -1))
            self.hashLb = wx.StaticText(self, -1, "Hash:", pos=(25, 92))
            self.hashTb = wx.TextCtrl(self, -1, "", pos=(80, 90), size=(560, -1))
            self.hashBt = wx.Button(self, label='Browse', pos=(640, 90), size=(70, 22))
            self.clearBt = wx.Button(self, label='Clear', pos=(710, 90), size=(70, 22))
            self.langLb = wx.StaticText(self, -1, "Lang:", pos=(25, 122))
            self.langCb = wx.ComboBox(self, -1, pos=(80, 120), size=(700, -1), choices=langs, value='ara Arabic')
            self.subsLst = wx.ListCtrl(self, -1, pos=(25, 160), size=(755, 139),style=wx.LC_REPORT|wx.BORDER_SUNKEN|wx.LC_SINGLE_SEL)
            self.searchBt = wx.Button(self, label='Search For Subtitles', pos=(25, 310), size=(377, -1))
            self.downBt = wx.Button(self, label='Download Selected Subtitle', pos=(402, 310), size=(377, -1))
            self.downPb = wx.Gauge(self, -1, pos=(25, 355), size=(753, -1))
            self.msgLb = wx.StaticText(self, -1, "", pos=(25, 395))
            #events
            self.hashBt.Bind(wx.EVT_BUTTON, self.OnOpen)
            self.searchBt.Bind(wx.EVT_BUTTON, self.OnSearch)
            self.clearBt.Bind(wx.EVT_BUTTON, self.OnClear)
            self.downBt.Bind(wx.EVT_BUTTON, self.OnDownload)
            self.nameTb.Bind(wx.EVT_TEXT, self.NameKeyPress)
            self.imdbTb.Bind(wx.EVT_TEXT, self.ImdbKeyPress)
            #listctrl configs
            self.subsLst.InsertColumn(0,"Movie Name",width=100)
            self.subsLst.InsertColumn(1,"Subtitle Name",width=360)
            self.subsLst.InsertColumn(2,"Movie Year")
            self.subsLst.InsertColumn(3,"Language")
            self.subsLst.InsertColumn(4,"User Rank")
            self.langCb.SetEditable(False)
            self.hashTb.SetEditable(False)

            #main window configs
            self.SetMaxSize((800, 460))
            self.SetMinSize((800, 460))
            self.subtitlesList = []
            self.SetTitle('SubGrabber By TaghoutiTarek@gmail.com')
            self.Centre()
            self.Show(True) 
            self.saveFilePath = ""
        #catch gui errors
        except Error, x:
           self.msgLb.SetLabel("An Error Ocurred : " + str(x))
    #text box on change event
    def OnClear(self, event):
        self.nameTb.SetValue("")
        self.imdbTb.SetValue("")
        self.hashTb.SetValue("")
        self.nameTb.Enable()
        self.imdbTb.Enable()
        self.hashBt.Enable()
        self.subsLst.DeleteAllItems()
        self.msgLb.SetLabel("An Error Ocurred : No save file path selected")
    def NameKeyPress(self, event):
        if(self.nameTb.GetValue() != ""):
            self.hashTb.SetValue("")
            self.imdbTb.Disable()
            self.imdbTb.SetValue("")
            self.hashBt.Disable()
        else:
            self.imdbTb.Enable()
            self.hashBt.Enable()
    def ImdbKeyPress(self, event):
        if(self.imdbTb.GetValue() != ""):
            self.hashTb.SetValue("")
            self.nameTb.Disable()
            self.nameTb.SetValue("")
            self.hashBt.Disable()
        else:
            self.nameTb.Enable()
            self.hashBt.Enable()
    #hash browse event
    def OnOpen(self, event):
        #show slect file dialog
        openFileDialog = wx.FileDialog(self, "Select Movie file", "", "","ALL files (*.*)|*.*", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        #close if cancel button activated
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        #return the selected file path    
        self.hashTb.SetValue(openFileDialog.GetPath())
        self.nameTb.SetValue("")
        self.imdbTb.SetValue("")
        self.nameTb.Disable()
        self.imdbTb.Disable()
    #save file dialog
    def OnSave(self, fileName, filePath, x):
        #clear save file path
        if(filePath == ""):
            self.saveFilePath = ""
        else:
            self.saveFilePath = filePath
        #show slect file dialog
        saveFileDialog = wx.FileDialog(self, "Save subtitle as", "", "","ALL files (*.*)|*.*", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        #set the default file name to the subtitle name
        saveFileDialog.SetFilename(fileName) 
        if(filePath != ""):
            saveFileDialog.SetDirectory(filePath)
        #close if cancel button activated
        if saveFileDialog.ShowModal() == wx.ID_CANCEL:
            return
        #return the selected file path    
        self.saveFilePath = saveFileDialog.GetPath()
        saveFileDialog.Destroy()
        if(self.saveFilePath != ""):
            self.msgLb.SetLabel("Downloading " + self.subtitlesList['data'][x]['SubFileName'])
            gz = urllib2.urlopen(self.subtitlesList['data'][x]['SubDownloadLink'])
            output = open(self.saveFilePath + ".gz",'wb')
            output.write(gz.read())
            output.close()
            with gzip.open(self.saveFilePath + ".gz", 'rb') as f:
                file_content = f.read()
                output = open(self.saveFilePath,'wb')
                output.write(file_content)
                output.close()
            if(os.path.isfile(self.saveFilePath)):
                os.remove(self.saveFilePath + ".gz")
                self.msgLb.SetLabel("Subtitle saved to " + self.saveFilePath)
            else:
                self.msgLb.SetLabel("An Error Ocurred : Saving file error")
        else:
            self.msgLb.SetLabel("An Error Ocurred : No save file path selected")

    #search button onclick event   
    def OnSearch(self, event):
        try:
            empty = False
            #setup the opensubtitles API
            server = ServerProxy("http://api.opensubtitles.org/xml-rpc")
            session =  server.LogIn("","","en","OSTestUserAgent")
            token = session["token"]
            #set the language code "code name"
            lang = self.langCb.GetValue().split(" ")[0]
            #initial empty list
            searchlist = []
            #search by name
            if(self.nameTb.GetValue() != ""):
                #lunch the query
                searchlist.append({'query':self.nameTb.GetValue(),'sublanguageid':lang})
            #search by imdb id
            elif(self.imdbTb.GetValue() != ""):
                imdb = str(self.imdbTb.GetValue())
                #if "tt" exist in the id delete it
                if("tt" in imdb):
                    imdb = imdb[2:]
                imdbid = unicode(imdb, 'utf-8')
                #if the id not numeric
                if(not imdbid.isnumeric()):
                    #show error message
                    self.msgLb.SetLabel("An Error Ocurred : " + imdbid + " Is not a valid IMDB ID")
                    return 
                #lunch the query
                searchlist.append({'imdbid':imdb,'sublanguageid':lang})
            #search by hash
            elif(self.hashTb.GetValue() != ""):
                #check if the file exist
                if(os.path.isfile(self.hashTb.GetValue())): 
                    #get the file hash
                    myhash = hashFile(self.hashTb.GetValue())
                    #get the file size
                    size = os.path.getsize(self.hashTb.GetValue())
                    #lunch the query
                    searchlist.append({'moviehash':myhash,'moviebytesize':str(size),'sublanguageid':lang})
                else: 
                    #if the file not exist show error message      
                    self.msgLb.SetLabel(str("An Error Ocurred : " + self.hashTb.GetValue()) + " Not exist")
            #if all fields are empty
            else:
                empty = True
            #get the search query result
            self.subtitlesList = server.SearchSubtitles(token, searchlist)
            #if there is a result
            if(len(self.subtitlesList) == 3):
                #prepare info message
                self.msgLb.SetLabel("Found " + str(len(self.subtitlesList['data'])) + " Subtitle(s)")
                #set progress bar range
                self.downPb.SetRange(len(self.subtitlesList['data']))
                #clear the listctrl
                self.subsLst.DeleteAllItems()
                #set the progress bar value to 0
                self.downPb.SetValue(0)
                #browse subtitles one by one
                for item in self.subtitlesList['data']:
                    #get the current subtitle infos
                    row = [item['MovieName'], item['SubFileName'], item['MovieYear'], 
                    item['LanguageName'], item['UserRank']]
                    #add the extracted infos the the listctrl
                    self.subsLst.Append(row)
                    #push the progress bar
                    self.downPb.SetValue(self.downPb.GetValue() + 1)
            #if the result is empty
            else:
                #show error message
                self.msgLb.SetLabel("Found 0 Subtitle")
            #API logout
            server.Logout(session["token"])
            if(empty):
                self.msgLb.SetLabel("An Error Ocurred : All fields are empty")
        #catch search errors
        except Error, v:
            #show error message
            self.msgLb.SetLabel("An Error Ocurred : " + str(v))
    #download button onclick event   
    def OnDownload(self, event):
        try:
            x = self.subsLst.GetFirstSelected()
            if(x > -1):
                if(self.hashTb.GetValue() == ""):
                    self.OnSave(self.subtitlesList['data'][x]['SubFileName'], "", x)
                else:
                    subFileName = os.path.splitext(os.path.basename(self.hashTb.GetValue()))[0]
                    subFileName += os.path.splitext(self.subtitlesList['data'][x]['SubFileName'])[1]
                    subDirName = os.path.dirname(self.hashTb.GetValue())
                    self.OnSave(subFileName, subDirName, x)
            else:
                self.msgLb.SetLabel("An Error Ocurred : No subtitle selected")
        except Error, e:
            self.msgLb.SetLabel("An Error Ocurred : " + str(e))
def main():    
    app = wx.App()
    Movie()
    app.MainLoop()    

if __name__ == '__main__':
    main()   
