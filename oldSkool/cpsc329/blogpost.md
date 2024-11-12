## Geoguessr and Location Data

If you've spent any time on a "tiktok-like" social media platform with scrolling and short videos, you've likely seen a young man who goes by the name Rainbolt. Certainly the world's best known *GeoGuessr* player, he's known for his flashy skillset. Throughout his career on these social media platforms, he's had different phases of content, each with their own implications on privacy.

As we know, postal codes, gender, and age can uniquely identify 80% of people in the States. A study done in Montreal showed that the number could be as high as 98% in Canada. (1)

Knowing all this, how could an attacker find a person's postal code from an Instagram post on a public account?

### Preface: GeoGuessr vs. Geolocating

Curiously, the main developments in geolocating have come from GeoGuessr. Due to the rules of the game, techniques that rely on memory are greatly emphasized, whereas others that require a bit of Googling and outside resources are not fully flushed out. In particular, Rainbolt uses techniques in the video above, like matching thicker branches on trees, which typically stay in the same place, and he compares them with current StreetView images from Google. All this to say that there is a great advantage in the resources available in geolocating traditionally, but this advantage is not yet developed.

A resource that is used for memorization purposes in GeoGuessr, but could be a reference for geolocating is the website geohints.com. It contains images with example street signs, bollards, language examples, and even quirks with certain cameras found on StreetView cars. With geohints, locating the country of a photo becomes far easier.

Finally, it's important to note that these techniques were developed to golocate images where a StreetView car can go. This means that most of our hints are developed around things found on roads. A photo taken in a public park, away from street signs and other typical Geoguessr hints will be far harder to geolocate with these hints.

Now let's jump in to some techniques that we can use to geolocate an image.

### Country-Guessing: 

Guessing countries is the main focus especially for beginner Geoguessr players, and is obviously an important step in geolocating a photo. Some tricks that help:

- Look for domain names of websites in the area. If you see .ca, .es, .dk, you immediately can tell what country you're in. (Bonus trivia: Without looking it up, what country has the .tv domain? It doesn't stand for television!)
- Bollards: You know those weird little markers that are on the sides of most roads inside and out of the city? Theses are called *bollards*, and it turns out that they're sometimes unique to a certain country. Often they're red and white, but if you see a white-on-white round bollard, you can be pretty certain the photo you're looking at is in France. TODO: Photo of French Bollard
- Road lines: Certain countries use yellow lines on streets, some use white, some use both. Certain combinations of road lines are more common than others, and so if we see a rare combination, we can narrow it down.
TODO: image
If we look at the above image for white sidelines + white and yellow middle, we see that there are few countries with this specific combination, and they are spread out among the globe. If we see this combination, we can usually use vegatation hints to immediately determine the country.

Numerous other tricks are available for detecting the country that a photo was taken in, but these are my personal favorites.

For the other sections, I'll be assuming that we know the country in question is Canada.

### Province-Guessing

Provinces are most easily guessed with cars. License plates are quite identifiable, if you can't see the province's name on the plate, the text color and shape of the plate will most likely give it away.

TODO insert plate photo 
https://i.ebayimg.com/images/g/6HsAAOSwAw5eV~EO/s-l1200.jpg

If your photo is on a road already, it's likely you already have a plate to look at,
but if not there are some distinctive differences in route markers from province to province. Of course, Halifax plates will sometimes make their way to Alberta, so it's nice to have confirmation. 

Beyond this, your best bet to determine the province is to compare vegetation and topological features. Most in Calgary will be familiar with the look of the praries, as well as the Rocky Mountains. Some travellers might recognize East Coast vegetation as well.

### City-Guessing

Guessing a city from a single photo can be incredibly easy to wildly difficult. If a building with a phone number is somewhere in the photo, the guess can be narrowed down to a city in Calgary and the US thanks to the area code. 

If you've narrowed down the province, and it's somewhere you're familiar with, you might even be able to instinctively make a call on the city based on "vibes." Parts of Edmonton are pretty easy to distinguish from Calgary, and other parts of the country will have similar distinguishing features and architecture.

Typically it's best to assume that photos are taken in large population centers, unless there's some reason to believe otherwise. High population density just means that there's a higher chance for a photo to be taken there. 

### Postal Codes / Down to the street

IF you've narrowed down the city, all it takes to find the street you're on is a single street sign. In geolocating, we have a luxury not found in GeoGuessr, Google Maps access! In high level GeoGuessr play, not only is Google Maps considered cheating, it's often slower in the long run to have to look up locations and switch tabs to get a perfect score. For us though, since time is not of the essence, we can take it slow for more precision.

If no street signs exist in the photo, we can again look for businesses and buildings that can identify location (Think elementary schools, family bakeries etc).

### Bonus exercises
A few months ago, I woke up early in the morning for an exam in the Fall semester. I was up earlier than typical for me, and so I got to see the sun rise. I took a picture and sent it to my friends in our group chat. When I got out of my exam, one of my friends had sent me a set of  GPS coordinates, and when I clicked them I saw the location where I had taken the photo.

[image] TODO
(The location; try it out! Put the coordinates in a reply to this post!)

How about this one? I was playing GeoGuessr (World map, mind you!) awhile ago and I was put in this Calgary location. This might have been the fastest perfect score I would ever get!

[image]TODO

### Sources
98% of Montrealers identified by age, gender, and postal code:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3151203/

Images for canada-specific information:
https://www.reddit.com/r/geoguessr/comments/102cobz/know_your_canada_a_guide_for_geoguessr_oc/

Rainbolt vid
https://www.tiktok.com/@georainbolt/video/7376415122945887531?lang=en

Study on AI geoguessr play
https://ieeexplore.ieee.org/abstract/document/9867085

Ukraine:
https://petapixel.com/2022/11/09/a-russian-missile-crew-was-geolocated-from-just-this-photo/

Geohints:
geohints.com
