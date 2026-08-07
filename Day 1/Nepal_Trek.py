print("Welcome to the Nepal Trek")
print("We have following Trek Package")
print("1. Annapurna \n 2. Everest \n 3. Langtang \n 4. Upper Dolpo  ")
print("Please enter a trek number ")

trek=int(input())

if trek==1:
    print("Annapurna Base Camp Trek \n "
          "Annapurna Base Camp Trek is one of the most popular and adventurous trekking journeys in Nepal. It takes trekkers through beautiful landscapes, traditional villages, green forests, and spectacular mountain views. The trek leads to the base camp of Mount Annapurna, one of the highest peaks in the world. Along the way, trekkers can experience local culture, warm hospitality, and diverse natural scenery. The trail passes through places like Ghorepani, Chhomrong, and Machhapuchhre Base Camp before reaching Annapurna Base Camp. The journey usually takes around seven to twelve days and offers unforgettable memories. Trekkers enjoy breathtaking views of snow-covered mountains, including Annapurna and Machhapuchhre. This trek is suitable for adventure lovers who want to explore the beauty, culture, and natural wonders of the Himalayas. It is a rewarding experience filled with excitement, challenges, and amazing moments. It also creates lasting memories for travelers seeking peace and connection with nature during trekking. ")
if trek==2:
    print("Everest Base Camp Trek  \n"
          "Everest Base Camp Trek is one of the most famous and challenging trekking adventures in Nepal. It takes trekkers to the base camp of Mount Everest, the highest mountain in the world. The journey offers stunning views of Himalayan peaks, including Everest, Lhotse, Nuptse, and Ama Dablam. The trail passes through beautiful Sherpa villages, ancient monasteries, rivers, and forests, allowing visitors to experience the unique culture and traditions of the local people. The trek usually takes around twelve to sixteen days and begins with a scenic flight to Lukla. Trekkers pass through important places like Namche Bazaar, Tengboche, and Gorak Shep before reaching Everest Base Camp. This adventure requires good physical fitness and determination but rewards travelers with unforgettable views and experiences. The Everest Base Camp Trek is a perfect choice for those who want to explore the Himalayas, enjoy natural beauty, and experience the spirit of adventure in Nepal. "
          )
if trek==3:
    print("Langtang Trek   \n"
          "Langtang Trek is a beautiful and peaceful trekking adventure in Nepal, known for its stunning mountain views, rich culture, and natural beauty. It takes trekkers through the Langtang Valley, surrounded by snow-covered peaks, forests, rivers, and traditional villages. The trek offers an opportunity to experience the lifestyle, traditions, and hospitality of the Tamang and Sherpa communities. The trail passes through places like Syabrubesi, Lama Hotel, Langtang Village, and Kyanjin Gompa, where trekkers can enjoy breathtaking views of mountains such as Langtang Lirung. Compared to other popular treks, Langtang is less crowded and provides a more peaceful experience. The journey usually takes around seven to ten days and is suitable for trekkers of different experience levels. Langtang Trek combines adventure, culture, and nature, making it an ideal destination for those who want to explore the beauty of the Himalayas and discover the hidden treasures of Nepal. ")
if trek==4:
    print("Upper Dolpo Trek  \n"
          "Upper Dolpo Trek is one of the most remote and adventurous trekking journeys in Nepal. Located in the western part of the country, it offers a unique experience of untouched landscapes, ancient culture, and stunning Himalayan scenery. The trek takes travelers through high mountain passes, deep valleys, beautiful lakes, and traditional villages. The region is famous for Shey Phoksundo Lake, one of Nepal’s most beautiful and deepest lakes. Trekkers can explore ancient Buddhist monasteries, including Shey Gompa, and experience the unique lifestyle of the Dolpo people. The trail passes through places like Phoksundo, Saldang, and high passes such as Kang La. Upper Dolpo Trek usually takes around eighteen to twenty-eight days and requires good physical fitness due to its challenging terrain and high altitude. This trek is perfect for adventure seekers who want to explore a remote Himalayan region, experience Tibetan-influenced culture, and discover the natural beauty of Nepal away from crowded trekking routes.")

print("For Booking please Enter your Information :- ")

name=input("Enter your name :-")
date=input("Enter your date :-")
country=input("Enter your country :-")
passport=int(input("Enter your passport :-"))
payment=int(input("Enter your Master Card Number :-"))

print("Name :- ",name)
print("Date :- ",date)
print("Country :- ",country)
print("Passport :- ",passport)
print("Payment :- ",payment)

print("For Confirmation please type trekking name 1 for annapurna 2 for everest 3 for langtang 4 for upper dolpo")

if trek==1:
    print("Please pay 1500")
if trek==2:
    print("Please pay 2500")
if trek==3:
    print("Please pay 1200")
if trek==4:
    print("Please pay 1000")
else:
    print("Wrong Information")


print("Type 1 for corfirmation\n 2 for cancelation")

type=input()
if type=="1":
    print("Trekking Booking Done")
else:
    print("Your Booking Canceled")

