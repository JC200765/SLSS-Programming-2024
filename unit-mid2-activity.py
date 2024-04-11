# Midterm U2
# Author: Justin
# 4/9/24
import random

Chinese_City = ["Harbin", "Shenyang", "Beijing"," Tianjin", "Jinan", "Changchun", "Nanjing", "Shanghai", "ShiJiaZhuang", "Fuzhou", "Guangzhou", "Zhengzhou", "Kunming", "Hangzhou", "Wuhan", "Xian", "Chongqing", "Chengdu", "Lhasa", "Urumqi", "Nanning", "Haikou" "Guiyang", "Hohhot", "Xining", "YinChuan"," Hefei", "NanChang", "ChangSha", "Taiyuan", "Lanzhou" ]

def city_suggestion(city):

    if city == "Harbin": 
        return "Harbin, the capital of HeiLongJiang Province in the Northernmost part of china includes many diverse Russian Architecture, you can visit the Saint Sophia's Church, Harbin Ice and Snow World (maybe in winter only, Bingxue Big World, Harbin Stalin Park, Sun island or Siberia Tiger Park "
    elif city == "Shenyang": 
        return "Shenyang is the Capital of China's NorthEast Provinve of Liaoning. In this city you visit the Zhaoling Tomb where the actual bodies of The first Qing Dynasty's emperor and empress are laid down at, Qipan Mountain,Mukden Palace and Shenyang Dongling Park"
    elif city == "Beijing": 
        return "Beijing is China's capital city and it holds vast knowledge in the terms of history, you can visit the Great wall of China, The Forbidden City, or visit the Body of Dictator Mao Ze Dong in the Mausoluem, of course you can also vist the Temple of Heaven.     (My First and favourite Home City"
    elif city == "Tianjin":
        return "Tianjin, is a port city that has 600 years of history, you visit Guwenhua street, Haihe river or my personal favourite Tianjin Binhai Aircraft carrier theme park "
    elif city == "Jinan":
        return "Jinan, the Capital of Shandong, the city is known for its natural springs. You can visit Chou ran Lou, Five Dragon Pool or Baotu Spings "
    elif city == "Changchun":
        return "Changchun is the Capital of Jilin province in china. when visiting there I suggest the following places: Nanhu Park, Changying Century City, Changchun Zoological and Botanical Park, The Former site of the puppet Manchukuo state department and etc"
    elif city == "Nanjing":
        return "Nanjing, the Capital of Jiangsu province has Dr. Sun Yat-sens Mausoleum, Memorial Hall of the Victims in Nanjing Massacre by Japanese Invaders,Qinhuai He, Porcelian Tower of nanjing and etc"
    elif city == "Shanghai":
        return "Shanghai is probably the most known chinese city, foreigners from Japan, Korea through Russia, Germnay and both Americas choose to work and live here to become the population of Shanghai. In Shanghai I recommend these places: The Bund, Yu Garden, Shanghai Disneyland park, Nanjing Lu and See the City Skyline at day and night to view Shanghai Oriental Pearl and Shanghai towers. "
    elif city == "ShiJiaZhuang":
        return "Capital of Hebei province, I recommend visiting: Bolin Temple, Tiangui Mountain and Kaiyuan Temple and etc"
    elif city == "Fuzhou":
        return "Capital of Fujian province, I recommend: Haitan Ancient City, Zuohai Park(Nort Gate, Tangyu Island , Langqidao and etc"
    elif city == "Guangzhou":
        return "Capital of Guangdong province I recommend: Chimelong water park, Chen Clan Ancestral Hall, Shamiandao Island, Canton Tower and etc (My second Chinese Home City"
    elif city == "Zhengzhou":
        return "Capital of henan province, I recommend: Shaolin temple, Zhenzhou yellow river scenic spots, zhongyuan tower, zhengzhou museum and etc"
    elif city == "Kunming":
        return "Capital of Yunnan province, I recommend visiting: Stone forest scenic, cui lake, yunnan ethnic village, jiu xiang rong dong, dongchuan red land and many more"
    elif city == "Hangzhou":
        return "Capital of Zhejiang province, I recommend: Xi lake, lingyin temple, xixi national park, Three pools Mirroring the Moon, hangzhou skyline and etc"
    elif city == "Wuhan":
        return "Capital of hubei province I recommend: yellow crane tower, donghu ntional wetland park, guiyuan temple, east lake cherry blossom park and etc"
    elif city == "Xian":
        return "Capital of Shaanxi province, I recommend: Emperor Qinshihuangs Mausoleum Site Museum, Giant wild doose pagoda, Fortifications of Xi'an, Ancient city wall, Huaqinggong relic site and etc" 
    elif city == "Chongqing":
        return "Chongqing is a city that is unheard of in western society, but in the modern day it as gained more popularity i recommend going to: Fengdu Ghost City Three Gorges Museum, Ciqikou(may be far, Three Natural Bridges, Hongyadong(View the city skyline at day and night, Jiefangbei CBD and etc (you may even see Mr. Mergens there viewing the city you can also plan a trip there with him."
    elif city == "Chengdu":
        return "capital of Sichuan province I recommend: Chengdu research Base of Giant Panda Breeding, Wenshu Yuan Monastry, Chuanxi Road and etc"
    elif city == "Lhasa":
        return "Capital of Tibet region of China, I recoomend: Potala Palace, Jokhang Temple, Sera Monastry, Ganden Monastry, Yerpa, Lukhang, Lalu Wetlands National Nature Museum Preserve and etc"
    elif city == "Urumqi":
        return "Capital of Xinjiang region of China, I recommend: Tianchi, Xinjiang International Dabazha Scenci Spot, Hongshan Mountain, and etc"
    elif city == "Nanning": 
        return "Capital of the Guangxi province, and very close to the Vietnm border i recommend: Yi Ling Yan, LongXiang Tower, Chaoyang Square, Qingxiu mountain Scenic Spot Zone, Nanhu Park, Xiningexpo Park and etc"
    elif city == "Haikou":
        return "Capital of Hainan Province which is the basic Hawaii of China i recommend: Guanlan Lake feng Xiaogang Film Commune, the tomb of Hairui, Trop Wildlife Park and Botancial Garden and etc (ou can honestly fly towards the other city in Hainan province called Sanya. over there you can do even more Hawaii stuff"
    elif city == "Guiyang":
        return "Capital of Guizhou Province, I recommend: Jiaxiu Building, Qingyan Ancient Town, Yelang Valley, Qianlingshan Park and etc"
    elif city == "Hohhot":
        return "Capital of Inner Mongolia region in China, I recommend: Dazhao Temple Inner Mongolia Historical museum, Five Pagoda Temple, Zhaojun Tomb, Bao'erhan Fota and etc"
    elif city == "Xining":
        return "Capital of Qinghai province I recommend: Kumbum Champa Ling, Dongguan Mosque, Riyue Mountain, Tulou Temple and etc"
    elif city == "YinChuan":
        return "Capital of Nngxia region, I recommend: Western Xia mausoleums, Zhenbeibao West Film Art Center, Shuidonggou Site, Suyukou Nation Forest park and etc "
    elif city == "Hefei":
        return "Capital of Anhui Province, a political economic place I recommend going to: Xiaoyaojin Park, Shushan Forest park, Hefei Science and Technology Museum, Huiyuan (South Gate, and many more"
    elif city == "NanChang":
        return "Nanchang the capital of Jiangsu Pronice, when visiting I recommend: Pavilion of Prince Teng, Bayi Square, Nanchnag, Haihunhou Tomb, Jiulong Lake, Poyang Lake National Nature Reserve and etc"
    elif city == "ChangSha":
        return "Changsha is the Capital of Hunan Province in China, when travling there I recommend going to: Yuelu Mountain, Juzizhou Island, Chagsha Window of the World, Hunan Martyr's Park, Kaifu Temple and etc"
    elif city == "Taiyuan":
        return "Taiyuan is the Capital of Shanxi, When visting I recommend going to these places: Jinci, Qiao Family Compound, Mengshan Giant Buddha, Congshan Temple and etc"
    elif city == "Lanzhou":
        return "Lanzhou is the Capital of Gansu Province of China, when going to the city I suggest seeing: Baitashan Park, Waterwheel expo Garden, Lanzhou Old Street, Lanzhou Museum and etc"

        


# Computer randomly prints out a city in china with its suggestion to here to see
# Randomly choose a city
chosen_city = random.choice(Chinese_City)

# Print out that city's name
print(chosen_city)

# Find the suggestion in the suggestions list
# Print it out
print(city_suggestion(chosen_city))

# Loop forever
    # user can either like ----> goes into a loop with infinite text of (I really recommend you going someday)
    # Ask the user if they like the suggestion
        # If they do, inifintely loop the text (I really recommend...)
    # or skip ----> leads to computer printing another city and its suggestion from the list
        # Else it repeats to give another suggestion







