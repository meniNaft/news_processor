import os
from dotenv import load_dotenv
from requests import post, HTTPError

load_dotenv(verbose=True)

NEWS_API_URL = os.environ["NEWS_API_URL"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]


def fetch_news(batch_num: int):
    payload = {
        "action": "getArticles",
        "keyword": "terror attack",
        "ignoreSourceGroupUri": "paywall/paywalled_sources",
        "articlesPage": batch_num,
        "articlesCount": 100,
        "articlesSortBy": "socialScore",
        "articlesSortByAsc": False,
        "dataType": ["news", "pr"],
        "forceMaxDataTimeWindow": 31,
        "resultType": "articles",
        "apiKey": NEWS_API_KEY
    }

    try:
        response = post(NEWS_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        if 'articles' in data:
            return data['articles']['results']
        else:
            print("No articles found.")
            return []

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

    return []


def get_mock():
    return [
        {
            "uri": "2024-12-583281968",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-22",
            "time": "16:40:27",
            "dateTime": "2024-12-22T16:40:27Z",
            "dateTimePub": "2024-12-22T16:39:48Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.infowars.com/posts/german-mother-mourns-loss-of-9-year-old-son-in-christmas-market-attack",
            "title": "German Mother Mourns Loss of 9-Year-Old Son in Christmas Market Attack",
            "body": "Germany continues to reel from a terror attack committed by Taleb A., a Saudi man who was granted German citizenship, after Taleb murdered five Germans and wounded over 200 on Friday night at the Magdeburg Christmas market. Now, the mother of the youngest victim, 9-year-old André, has posted a heart-wrenching message on Facebook following the loss of her son.\n\n\"André didn't do anything to anyone -- why you, why?\" With these words, Désirée G. wrote her goodbyes to her son on Facebook. She also shared a photo of him.\n\n\"Let my little teddy bear fly around the world again,\" she begins her post. She wrote that André is now with his grandparents in heaven.\n\n\"They missed you very much, as much as we miss you here now.\" she added.\n\nTaleb A. drove a rented BMW into the crowd at full speed, killing five but also injuring another 200 people. There are still dozens fighting for their lives. So far, 41 people were seriously injured in the attack,\n\nOne woman, Anne, who was hit by the driver and knocked unconscious, told Bild newspaper: \"I woke up and thought I was in a dream.\" She still has a bloodshot eye from attack, however, her husband suffered a far worse injury to his thigh, saying that his flesh was \"literally ripped out.\" However, they were reunited when Anne regained consciousness when volunteers helped them find each other at the scene of the attack, and both expressed their happiness at being alive.\n\nNotably, German Christmas markets are already treated like fortresses, but Taleb A. found the only spot in the entire market that did not have a barrier, which was there to allow emergency vehicles and personnel to gain access to the market in the case of an emergency.\n\nThere is currently a debate raging about the man's motives, with a number on the right trying to claim Taleb A.is a secret Islamist. However, it appears from his own messages that he was furious that Germany was not granting asylum to Saudi refugees. He is on record threatening Germany and ethnic Germans with \"slaughter\" for not helping Saudi ex-Muslims.\n\nSome on the left are trying to tie him to the AfD, since he expressed support for the party in one of his posts. However, skeptics cite him saying he was a \"leftist\" in a video, that the AfD is strictly against mass immigration and granting asylum to those with a criminal record such as Taleb A., and that his multiple threats against Germans stands in complete contrast to the AfD's political platform, which seeks to block foreigners such as Taleb from entering the country entirely.\n\nRegardless of his motives, the man has a criminal history and had an open extradition request from Saudi Arabia -- yet he was still granted asylum and citizenship. In Germany, he faced a criminal complaint dating back to 2013 for threatening behavior. According to the Spiegel, Taleb A. had was found guilty in a district court in Rostock and sentenced to a fine of 90 daily rates on Sept. 4, 2013, for \"disturbing the public peace by threatening to commit criminal offenses\".\n\nIn addition, despite the German authorities at the BAMF being warned about his threatening statements against Germans by X users, no action was taken.\n\nIn short, it was a catastrophic failure in terms of migration and security policy from the German authorities. This failure has even caught the attention of Elon Musk, who shared a thread documenting the man's disturbing history in Germany and a lack of action from authorities.\n\nTaleb A. worked as a specialist in psychiatry and psychotherapy at a correctional facility in Bernberg. Shortly before the attack, he was on sick leave for several weeks.\n\nGermans have had their houses raided for calling Economic Minister Robert Habeck an \"idiot,\" and hundreds have faced prosecution for such insults. However, Taleb A. was saying just before the attack on X \"I assure you that revenge will 100 percent come soon. Even if it costs me my life.\"\n\nThere was no security response to his threats. In fact, police have been instead harassing grandmas at Christmas markets, a potential source of wasted resources that could have been put to work stopping an actual terror attack.\n\nTaleb A.is charged with five counts of murder and 205 counts of attempted murder. While Taleb A. is alive, Germans are mourning the deaths of their loved ones. Writing to her dead son André, Désirée G. ends her farewell post by writing: \"You will always live on in our hearts. I promise you that.\"",
            "source": {
                "uri": "infowars.com",
                "dataType": "news",
                "title": "Infowars"
            },
            "authors": [],
            "image": "https://imagedelivery.net/aeJ6ID7yrMczwy3WKNnwxg/3168c99d-690b-4b26-b635-721cf9089700/w=800,h=450",
            "eventUri": None,
            "sentiment": -0.1764705882352942,
            "wgt": 92912,
            "relevance": 18
        },
        {
            "uri": "2024-12-582651403",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-21",
            "time": "17:26:24",
            "dateTime": "2024-12-21T17:26:24Z",
            "dateTimePub": "2024-12-21T17:25:16Z",
            "dataType": "news",
            "sim": 0.4235294163227081,
            "url": "https://www.infowars.com/posts/christmas-market-attack-suspect-was-saudi-arabian-leftist-asylum-activist-promoted-by-bbc",
            "title": "Christmas Market Attack Suspect Was Saudi 'Leftist' Asylum Activist Promoted By BBC",
            "body": "Suspect was also reportedly a Zionist who supported \"Greater Israel.\"\n\nThe suspect behind the Christmas Market terror attack in Germany that left multiple people dead and hundreds injured was a leftist Saudi national who was promoted by the BBC for his efforts to help asylum seekers into Germany.\n\nThe suspect, identified by German authorities as 50-year-old Taleb Al Abdulmohsen, was taken into custody Friday after driving a rented car into a crowd gathered for a Christmas market in Magdeburg that killed 5 and injured over 200.\n\nTaleb was an asylum seeker who arrived in Germany in 2006 after allegedly fleeing Saudi Arabia for fear of persecution for being an atheist.\n\nHe was granted asylum in Germany in 2016 and had been living in the town of Bernburg as a psychiatrist.\n\nThe BBC in 2019 featured Taleb describing how he ran a refugee program to help ex-Muslim women flee Sharia Law and the Saudi government's human rights abuses.\n\nThat same year, in an interview with FAZ, Taleb claimed he was \"the most aggressive critic of Islam in history,\" and that he was ostracized from the Muslim community in Germany over his atheism.\n\nHe also detailed his move to become a pro-asylum activist in Germany in the interview.\n\nFollowing his identification as the suspect behind the Christmas market attack, FAZ added an editor's note saying, \"This interview with Taleb Al A. was published in June 2019. Entries of the alleged assassin in the social media indicate that he has also been increasingly quarreling with Germany and its migration policy over the five and a half years since then. There are also signs of persecution delusions. Nothing of this was felt in 2019. Here is the unchanged wording of the conversation.\"\n\nAlthough the legacy media has focused on statements Taleb made in support of the populist right-wing Alternative for Germany (AfD) party over its critiques of mass immigration, he apparently considered himself to be a leftist.\n\n\"Taleb A. said in the interview that he was not a right-winger and described himself as a leftist,\" Der Spiegel reported.\n\nThe German government repeatedly ignored warnings from Saudi Arabia about Taleb as well as requests for his extradition last year.\n\nTaleb told German authorities that his motive for the attack was related to \"dissatisfaction with the way Saudi Arabian refugees are treated\" in Germany.\n\nDespite his purported atheism, Taleb also appears to be a Zionist who expressed his support for \"Greater Israel\" on social media.\n\nWhen Taleb's background was still unclear, the media was perfectly content reporting that a car was responsible for the horrific attack at the Christmas market.",
            "source": {
                "uri": "infowars.com",
                "dataType": "news",
                "title": "Infowars"
            },
            "authors": [],
            "image": "https://imagedelivery.net/aeJ6ID7yrMczwy3WKNnwxg/225c1d6f-6756-49ef-3fe8-2569b7300a00/w=800,h=450",
            "eventUri": "eng-10192203",
            "sentiment": -0.2705882352941177,
            "wgt": 92884,
            "relevance": 1
        },
        {
            "uri": "2024-12-577671498",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-16",
            "time": "19:09:49",
            "dateTime": "2024-12-16T19:09:49Z",
            "dateTimePub": "2024-12-16T19:09:36Z",
            "dataType": "news",
            "sim": 0.5921568870544434,
            "url": "https://www.infowars.com/posts/unidentified-drones-in-americas-skies-smells-like-a-False-flag",
            "title": "Unidentified Drones In America's Skies? Smells Like A False Flag...",
            "body": "Drone sightings have exploded across the country involving a wide variety of devices - but the incidents that concern me the most are those involving the SUV-sized UAVs in places like New Jersey.\n\nThe term \"False Flag\" gets thrown around rather haphazardly these days and it's important to recognize that a real False flag requires a particular end result - The public blaming the wrong culprit for an event that someone else (usually our own government) perpetrated. When it comes to the increasing fervor over major drone activity across the US, I have very little doubt that what we are witnessing is a False flag scenario.\n\nFirst, let's outline what has happened so far: Drone sightings have exploded across the country involving a wide variety of devices - but the incidents that concern me the most are those involving the SUV-sized UAVs in places like New Jersey. The sightings have been happening for months. US government agencies including the FBI, DHS and national security officials claim they have no idea who is behind this activity, even though drones have been seen operating over highly protected areas like US military bases.\n\nThere's a lot of information to be gleaned here if you know what you're looking for. I have written extensively about drones and drone warfare in my survival newsletter over the years, primarily on new developments in the technology and ways for civilians to defeat that technology. However, I have also written on how civilians can use drones for their own self defense.\n\nI know enough about tracking technology to say with relative certainly that officials are lying about the drones over New Jersey, and probably about most of the covert drone activity in other parts of the country. They know who is controlling these drones, and it's most likely our own government. What we are witnessing is some form of False flag in progress.\n\nFirst and foremost, drones can indeed be tracked rather easily depending on where they fly. Remote signals going back to the operator can be tracked with the right equipment. The stronger the remote signal the easier it is to find the operator. In New Jersey, for example, US Air Force Joint Base McGuire-Dix-Lakehurst partnered with AeroDefense, a local business specializing in tracking technology and drone detection, to produce a system to track drones across the installation as well as pinpoint perpetrators who fly them. They started this program back in 2020.\n\nDrone company DJI, which controls around 90% of the consumer drone market, has their own proprietary drone tracking technology that can be purchased by governments and various agencies. There's likely dozens more companies out there right now producing similar products to the DJI tracking tech.\n\nUnder new FAA regulations instituted this year, all drones operating in US air space (except very small drones) are required to carry a Remote ID module which broadcasts operator information and location. Most drones now have Remote ID integrated into their software and removing it can be a pain. For example, DJI drones are basically no longer used by Ukrainian forces because the built-in Remote ID gives away their positions. They now build most of their drones from scratch.\n\nThere are ways around drone tracking (to a point). Remote ID spoofing devices can be built and programmed for as little as $20. These broadcasting modules can create the illusion of dozens of drones in the sky with False operator data included. Anyone trying to use Remote ID tracking to find you will have no idea which drones are real and which are fake.\n\nDrone signal repeaters (which function much like ham radio repeaters) are not uncommon and are used in Ukraine by both sides to help confuse tracking attempts. Signal repeaters and antennas are easy to hide, and pinpointing an exact location is difficult. In Ukraine, trackers would simply find a general area where the antenna or operator might be and then hit it with artillery. If they only hit a repeater, then the operator is out about $200 and that's it.\n\nThe Russians use drones connected to long spools of fiber optic cable which allows them to send the devices into areas protecting by jamming. The direct connection also keeps the operators from being tracked.\n\nThen there are drones with AI software which bypass a lot of tracking tools. If the drone is controlling itself then there's no operator signal to trace. The drone might be broadcasting a video signal but that's not going to give up the location of the people who deployed the drone.\n\nMost of these techniques would never be used by common civilians or even small terror groups (AI flight software in particular would only be used by governments). On top of that, access to large drones or car-sized drones is very rare for civilians and requires extensive permits. The cost of such devices is prohibitive (tens-of-thousands or hundreds-of-thousands of dollars depending on the drone).\n\nMy point is, there is no way civilian operators or small terror groups are behind the majority of these events. The level of sophistication involved here requires military or government agency oversight. Beyond that, there aren't enough countermeasures in the world to prevent tracking over sensitive government locations. The US military and DHS have extensive means to track down drones (especially large drones) flying in close proximity to bases and protected sites.\n\nTriangulation would not be hard given the drone operators would have to fly through the middle of multiple detection equipped facilities. And, even if the drones are AI operated, large drones are not very fast or nimble. They could be followed without much trouble by helicopters or other drones.\n\nLack of public knowledge on this issue is being exploited by government officials and the media. I have seen multiple agency representatives claim that there's \"not enough restrictions in place\" to keep the threat of domestic drones in check. I have also seen government reps claim these drones are being operated by a foreign enemy like Iran. Recently, at least two men were arrested for flying a small drone too close to an airport in Chicago - Federal agencies and the media have tried to link these men to the covert drone sighting across the country when it's likely they have nothing to do with the situation.\n\nMisinformation like this suggests an attempt to pin the drone activity on civilian sources, or, a foreign adversary working with civilian sources. In other words, they are preparing the ground for one of two outcomes: More aggressive restrictions on civilian drones, or, an drone attack that is blamed on a foreign government.\n\nThe size of the drones is what worries me most. If the goal of a foreign government was to monitor sensitive sites and collect information, they wouldn't use car-sized drones. Large drones would be too easy to trace. They would use small mid-range drones outfitted with thermal that fit in a backpack.\n\nBut, our own government could fly fleets of large drones over cites and military bases with impunity. If our government wanted to, say, blow up a sacrificial military facility, damage a nuclear power plant or hit a civilian center, car-sized drones would be very useful because they are designed to carry considerable weight. Drones like those sighted over New Jersey could carry 500-1000 pounds of ordnance (maybe more). A swarm of these drones could cause total havoc in a heavily populated area.\n\nI worry about this outcome because the Biden Administration and the globalist establishment have been very active in the past several months trying to create as many ignition points for world war as they possibly can before Donald Trump takes office in January. A False flag at this time makes perfect sense.\n\nMy second theory is based on the strange comments by defense officials linking the activity to lack of restrictions on the civilian drone market. As noted, there is NO WAY civilians are flying car-sized drones in US airspace over protected sites without being followed. The drones are too expensive, too big to move around without people noticing and that kind of operation requires insider knowledge of DoD and DHS tracking methods.\n\nSome have speculated that there may be an agenda to get legislation (like a new Patriot Act) passed in the near future. I believe this may be a ploy to get traction on legislation restricting or banning civilian ownership of drones. Some people might be skeptical about that idea, but consider for a moment how useful drones are to a potential populist rebellion...\n\nFor over a century, governments and national armies have had a monopoly on aerial surveillance and the ability to engage enemies from the sky. With the invention of drones many patriots and survivalists have viewed the technology as the biggest threat to future attempts at rebellion against the establishment. The devices are cheap to produce, can operate in forests and urban environments and even small drones can carry enough explosives to maim or possibly kill with precision.\n\nIn the past, smaller forces using asymmetric tactics could still gain the upper hand against governments, even when fighting an advanced military with air superiority. Drones are now treated as the end game for insurgencies. But the truth is quite the opposite; drones are the end game for standard armies and a huge advantage for asymmetric rebellions. Drones are the biggest game changer in warfare for civilians since the invention of the repeating rifle.\n\nWe have seen the face of combat change dramatically in the war in Ukraine as drones become increasingly vital for both sides. Medium-sized drones have disrupted typical maneuver warfare tactics using high explosives to disable armored columns. Small drones allow operators to monitor the battlefield from the sky for miles and make discreet troop movements impossible.\n\nDrones can be easily used by civilians for the same purposes. For the first time ever, patriots have access to the air for surveillance and defense. I would not be surprised to see governments fabricate reasons why the technology \"needs to be banned\" - They will try to sell the American people on the idea that drones are a danger to public safety, even if that requires bankrolling a terror attack to frighten people into compliance.\n\nIn either case - A trigger for WWIII or a test case for banning the civilian drone market, the establishment gains an advantage. As far as I can tell, no one else benefits from these drone incidents. All signs point to a False flag. If this reality is exposed widely enough, I expect that the government will finally admit that they were behind the drone flights, but only as an effort to \"protect the public\" from an insidious threat that they could not tell us about beforehand.",
            "source": {
                "uri": "infowars.com",
                "dataType": "news",
                "title": "Infowars"
            },
            "authors": [],
            "image": "https://imagedelivery.net/aeJ6ID7yrMczwy3WKNnwxg/ab587dcc-fee0-4264-6cac-a99552cad100/w=800,h=450",
            "eventUri": "eng-10172147",
            "sentiment": 0.05882352941176472,
            "wgt": 92781,
            "relevance": 1
        },
        {
            "uri": "2024-12-577693303",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-16",
            "time": "19:40:36",
            "dateTime": "2024-12-16T19:40:36Z",
            "dateTimePub": "2024-12-16T19:39:51Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.infowars.com/posts/a-vexed-question",
            "title": "A Vexed Question",
            "body": "The who, what, where, why and how of demographic change are vexed questions. The who, in particular, and the why.\n\nFor some, like Renaud Camus, the man who actually coined the term \"the Great Replacement,\" mass demographic change in the West is not the product of any kind of conspiracy. There is no \"who\" as such directing the importation of hordes of Third World people into the nations of Europe, North America and the Anglosphere.\n\nInstead, for Camus, the Great Replacement is simply the result of the spread of a way of thinking he terms \"replaceism\": a belief that, ultimately, all people are just interchangeable and therefore there is no such thing as, say, genuine national or ethnic identity that should or even could be preserved.\n\nWe might call a variant of this the \"magic soil\" theory of identity. There is nothing, nothing apart from an official legal process, that can stop a Nigerian who lands in France or the UK from becoming French or British or Welsh or even, like me, Cornish.\n\nCamus sees \"replaceism\" as emerging and growing due to the profound social, economic and spiritual changes of the modern era -- everything from the Reformation and the Enlightenment to the spread of industrialisation, capitalism, mass democracy, mass education and mass entertainment.\n\nThe television is as much to blame as any politician.\n\nThe \"why\" that follows from this de-centered \"who\" is clearly also de-centered. \"Replaceism\" is the logic of the modern liberal world. It's unavoidable. There isn't any malice behind it. It has terrible effects, of course, and it's destroying the West, but the will behind it is blind and unfeeling.\n\nIt's not personal, however much you might hate it.\n\nMany people who criticize or fête Camus don't actually seem to know this: that he identifies no single group that is to blame, even if he holds politicians and the media in deep contempt -- as he, and we, should -- for their cowardice and self-serving behaviour. People who describe Camus as a racist or white supremacist or even right wing usually tend to ignore what he's actually saying.\n\nThe opposite tendency -- well, we know what that looks like, don't we? An identifiable group and a clear sense of malice towards the people of the West. Often, that group is said to be some tribe of wandering desert folk, like the Bedouin or the Bakhtiari nomads of Iran. These people, from a deep historical antipathy for settled agricultural peoples and in particular Christians, have decided to subvert and overthrow their societies and civilisation from within.\n\nThis account, by contrast, is very personal.\n\nEverywhere we look, at all the institutions that are bringing on the Great Replacement -- from the government departments and the think-tanks to the religious NGOs bussing migrants and the universities indoctrinating Westerners to hate themselves, their culture and their history, not to mention the companies sapping the younger generation's desire to reproduce with porn, dating apps and parasocial smut websites like OnlyFans -- everywhere we look we detect the sandy fingers and the mint-yoghurt smell of a Bedouin or some such. Or so the theory goes.\n\nThe implication, of course, is that any attempt to reverse mass immigration and mass demographic change must therefore focus on this group primarily, on dislodging them from their secret control of the West.\n\nThe truth, I think, is somewhere in between. We absolutely must reckon with enormous impersonal changes that have taken place and made it possible to think a Nigerian can become a Briton simply on the basis of a citizenship test. The way we think about nationality and identity has changed tremendously, and it has changed tremendously over a long span of time, centuries in fact, without any obvious direction except its own inner logic, which draws its sources, as Camus shows, from many different places and things.\n\nAt the same time, though, we should also be alive to the genuine malice and wilfulness that seem to motivate official policies of mass immigration in Western nations.\n\nAs a Brit, I well remember the shocking revelations made by Andrew Neather, a former advisor to Tony Blair's New Labour government, which was responsible for introducing mass immigration to Britain beginning in 1997. In about 2010, Neather told a British newspaper that the policy had been specifically formulated to \"rub the right's nose in diversity\" and change the social fabric of Britain forever, so that a truly conservative government could never again be elected.\n\nThere was outcry at the time, and official denials, but why would Neather have made it up? He was simply being honest. Peter Mandelson, a New Labour grandee, said the government actually sent search parties out to Eastern Europe to get people to come to the UK, despite the fact they weren't really needed to fill jobs in the economy.\n\nIf you're an American, or even an observer from the other side of the Pond like me, it's hard to look at what happened in Springfield, Ohio or Charleroi, Pennsylvania or across the entire nation since 2021 and not see a deliberate plan to displace real Americans with foreigners, for political purposes (winning the election) at the very least.\n\nBut there's malice too, no doubt. The absurd, grotesque spectacle of 20,000 cat-eating Haitians being dumped in a small Midwest town bespeaks, to me, a deep hatred of actual Americans that is confirmed by everything else the Biden admin has done for the last four years.\n\nAnyway, I say all of this as a long prelude to the following observation, or rather question: Why is it that, as demographic replacement really begins to bite across the West, governments are so keen to bring in euthanasia services that will only be used by the natives?\n\nFrom the outside, it certainly looks like an evil twist to me, but could it just be happenstance.\n\nWith the release of the latest figures from Canada, which has gone turbo-Great Replacement under its oleaginous Prime Minister Justin Trudeau, we do at least know that this is the case: that white people are the overwhelming constituency for legal euthanasia.\n\n\"Medically assisted dying\" or \"MAiD\" is used almost entirely by white Canadians. Ninety-six percent of cases are white Canadians. White Canadians make up 67% of the population.\n\nCanadian doctors are now killing 15,000 people a year, more or less all of them white. That's 5% of all deaths in a given year. Many of these people are poor and ill, abandoned by a government and a welfare system that are only too happy to accommodate people with no ties whatsoever to Canada -- to house, feed, employ and care for their health, on the basis of no prior relationship at all.\n\nSome of those who seek MAiD are even veterans who have served Canada in the military. Instead of being offered wheelchair ramps for their homes and new prosthetics, they're offered a lethal injection.\n\nIf other Western countries that have legalised euthanasia -- Austria, the Netherlands, Spain, Belgium -- released statistics by ethnicity, I'm sure exactly the same pattern would be visible, just as starkly.\n\nAnd it's not just older people either. As we know from the case of Shanti de Corte or more recently the Belgian woman known only as \"Laura,\" it's young people too. Young people who despair at the state of the world and their countries, whether they know the real reasons for their despair or not. Shanti de Corte suffered PTSD after surviving an Islamist terror attack in Brussels.\n\nTo tell you the truth, I'm not sure what to make of this. But I do know it troubles me deeply. Malice or impersonal logic -- either way, it amounts to the same thing, and it's not good.",
            "source": {
                "uri": "infowars.com",
                "dataType": "news",
                "title": "Infowars"
            },
            "authors": [],
            "image": "https://imagedelivery.net/aeJ6ID7yrMczwy3WKNnwxg/13c3d4ef-8b2b-4709-064c-1ff94dbfb800/w=800,h=450",
            "eventUri": None,
            "sentiment": 0.09019607843137245,
            "wgt": 92768,
            "relevance": 1
        },
        {
            "uri": "8429097876",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "05:50:27",
            "dateTime": "2024-11-26T05:50:27Z",
            "dateTimePub": "2024-11-26T05:49:25Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://aninews.in/videos/national/2611-terror-attack-maha-cm-shinde-deputy-cms-fadnavis-ajit-pawar-pay-tribute-on-anniversary/",
            "title": "Asia's Leading News Site - India News, Business & Political, National & International, Bollywood, Sports | ANI News",
            "body": "Mumbai, Nov 26 (ANI): November 26, 2024 marked the 16th anniversary of the 26/11 Mumbai terror attack that shook the nation. On the occasion, Maharashtra Guv Radhakrishnan paid floral tributes to Bravehearts at Martyrs' Memorial on premises of Police Commissioner's Office. Maharashtra CM Eknath Shinde also paid tribute to the Bravehearts at the Memorial on the 16th anniversary. Further, Maharashtra Deputy CMs Devendra Fadnavis, Ajit Pawar paid homage to the Bravehearts.",
            "source": {
                "uri": "aninews.in",
                "dataType": "news",
                "title": "Asian News International (ANI)"
            },
            "authors": [],
            "image": "https://d3lzcn6mbbadaf.cloudfront.net/media/details/anilogo.jpg",
            "eventUri": None,
            "sentiment": -0.2,
            "wgt": 10378,
            "relevance": 1
        },
        {
            "uri": "8430106473",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "17:06:01",
            "dateTime": "2024-11-26T17:06:01Z",
            "dateTimePub": "2024-11-26T17:05:40Z",
            "dataType": "news",
            "sim": 0.6901960968971252,
            "url": "https://www.cbsnews.com/news/israel-hezbollah-ceasefire-netanyahu-war-lebanon-gaza-hamas/",
            "title": "Israel-Hezbollah ceasefire deal to halt war in Lebanon expected within hours",
            "body": "Israel and the Iran-backed Hezbollah group appear set to halt the war that has killed almost 3,800 people in Lebanon over the last year and left about 16,000 others wounded. President Biden is expected to announce Tuesday that the U.S. and France secured a ceasefire in Lebanon, ending the fighting between Israel and Hezbollah, according to a U.S. official.\n\nThe full and permanent ceasefire would end the deadliest war in Lebanon since its civil war ended in 1990.\n\nUnder the deal, a full and permanent ceasefire would be implemented immediately. There will be 60 days permitted for the full withdrawal of Israeli forces -- a gradual withdrawal to allow the Lebanese forces to mobilize and move in to secure the area, but the trigger time is immediate, set to take effect later Tuesday.\n\nThe first peel-off of Israeli troops was to begin within the next 10 days.\n\nHezbollah is expected to pull its forces and heavy weapons back about 20 miles from the Israeli border, to the Litani River.\n\nAn official in Netanyahu's office told CBS News that the prime minister had convened the country's security cabinet to discuss the proposal. The cabinet must approve any ceasefire agreement. Netanyahu was also holding meetings Tuesday in Tel Aviv with various government ministers, lawmakers, and mayors from some of the northern towns that have been evacuated for months.\n\nLebanon's government also had to unilaterally approve the deal on Tuesday, but the U.S. official said that was expected.\n\nNetanyahu was to address his country at 8 p.m. local time (1 p.m. Eastern) on Tuesday, according to his office, with President Biden then delivering remarks about the agreement in Washington within a few hours.\n\nHezbollah, a powerful military and political entity in Lebanon that has long been designated a terrorist group by both the U.S. and Israel, started firing rockets into Israel on Oct. 8, 2023, in support of its Hamas allies who sparked the war in Gaza with their terror attack the previous day.\n\nIsrael carried out airstrikes on purported Hezbollah targets for months, but in September it dramatically escalated its assault on the Iranian proxy group, including by launching ground operations in the south of Lebanon.\n\nCBS News correspondent Debora Patta said rockets were still flying in both directions over Israel's northern border on Tuesday, with Israel and Hezbollah trading some of their heaviest fire to date, even as diplomats push for peace.\n\nUnder the proposed deal, Lebanese forces and United Nations peacekeepers are expected to jointly patrol southern Lebanon to ensure the terms of the agreement are adhered to. Earlier reports suggested the southern region would be monitored by a multi-nation committee, which would include both the U.S. and France.\n\nMiddle East expert Danny Citrinowicz, a fellow at the Atlantic Council think tank, said the deal looked \"good on paper,\" but added that until it was implemented, \"it would be hard to know whether Israel can really build on these kind of guarantees coming from the U.S. administration.\"\n\nAfter more than a year of crossfire, more than 1.2 million people have been displaced from their homes in Lebanon, along with at least 60,000 from towns and villages in northern Israel. They're all desperate to go home, and Israeli Prime Minister Benjamin Netanyahu has long said the chief objective of the war with Hezbollah, from his government's standpoint, has been to enable them to do so.\n\nWhile a deal with Hezbollah appeared closer than ever, negotiations for a ceasefire in Israel's war with Iran's other proxy force in the Gaza Strip, Hamas - have gone nowhere.\n\nMany in the decimated Palestinian territory are hungry, and recent rainstorms have made living conditions there even worse. A winter chill has set in, and there were reports of a fresh Israeli strike killing about 15 people Tuesday in Gaza City.",
            "source": {
                "uri": "cbsnews.com",
                "dataType": "news",
                "title": "CBS News"
            },
            "authors": [],
            "image": "https://assets2.cbsnewsstatic.com/hub/i/r/2024/11/26/1f120a24-3a6b-4cd2-87f1-3ef8aedda628/thumbnail/1200x630/2a916451b08478fe5ccb70cf87cadb79/israel-tank-lebanon-hezbollah.jpg?v=e3aa8b4a58817620ee227c79202c9709",
            "eventUri": "eng-10117744",
            "sentiment": -0.09019607843137256,
            "wgt": 722,
            "relevance": 1
        },
        {
            "uri": "8436328554",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-30",
            "time": "16:20:05",
            "dateTime": "2024-11-30T16:20:05Z",
            "dateTimePub": "2024-11-30T16:19:21Z",
            "dataType": "news",
            "sim": 0.9450980424880981,
            "url": "https://nypost.com/2024/11/30/us-news/nyc-staffer-paid-to-promote-diversity-caught-ripping-down-israel-hostage-poster-allegedly-assaulting-person-filming-it/",
            "title": "Exclusive | NYC staffer paid to promote diversity caught ripping down Israel...",
            "body": "An Adams administration staffer whose mission includes fostering \"unity\" and bridging \"cultural divides,\" is under fire for ripping down an Israeli hostage poster -- and then allegedly assaulting an outraged eyewitness, The Post has learned.\n\nNallah Sutherland, a special event coordinator for the Mayor's Office of Special Projects and Community Events, was spotted earlier this month tearing down the poster from an Upper East Side light pole, ripping it up and dumping it in a trash bin, according to video posted online by the nonprofit StopAntisemetism.\n\n\"It's an appalling act of antisemitism,\" said the nonprofit's founder Liora Rez, who demanded Adams immediately fire Sutherland.\n\nBut Sutherland, 25, only got a slap on the wrist by her bosses -- who merely required her to take \"multicultural training\" and added a disciplinary note to her permanent work file, a City Hall source told The Post.\n\nFootage of the Nov. 2 incident at the corner of York Ave and East 84th Street begins with Sutherland tearing off the poster and tossing it in the trash.\n\n\"Is there a reason you're taking those down?\" asks an eyewitness about the poster, part of a public art campaign to raise awareness of Israeli and American hostages taken captive by Hamas during its Oct. 7, 2023 terror attack on the Jewish state.\n\n\"Those were hostages. They were taken by terrorists,\" adds the eyewitness, according to the 20-second clip he recorded.\n\nSutherland then walks toward the man and swipes his phone with her right hand, briefly knocking it out of focus, the video shows.\n\n\"That's assault actually. You know that, right?\" the man responds to Sutherland, who smirks and walks away, the video shows.\n\nSutherland began working for Adams - a staunch Israel supporter - in 2023. She earns $61,135-a-year helping plan celebrations he hosts at Gracie Mansion and at other sites to honor the diverse city's many ethnic groups, records show.\n\nShe's part of a team whose job is to \"bridge cultural divides ... and support key city initiatives that help provide a source of strength, unity, and resilience to New Yorkers across all communities within the five boroughs and beyond,\" according to her office's website.\n\nIn May, the office organized a Jewish heritage celebration hosted by Adams at Gracie Mansion. The guest speakers included Shoshan Haran, who along with her daughter and two grandchildren, were taken hostage by Hamas and released 50 days later.\n\n\"It's extremely hypocritical that someone who supports the murder of anyone still has a job, much less in a department that plays a vital role in our city's diversity efforts -- despite the fact that she cannot tolerate innocent Jews who were kidnapped by Hamas,\" said Councilwoman Inna Vernikov (R-Brooklyn) after being told about Sutherland's action.\n\n\"Decisive action must be taken to purge this disgusting pro-jihadist sentiment from\" city government \"once and for all,\" added Vernikov, who is Jewish.\n\nThe eyewitness, who is Jewish and didn't report the incident to authorities, wants to remain anonymous out of fear of retribution considering antisemitism cases are soaring statewide.\n\n\"It's a sad state of affairs when the victim doesn't have trust in the NYPD or\" soft-on-crime Manhattan District Attorney Alvin Bragg \"to properly investigate\" hate crimes,\" said Rez. \"There's no trust in the authorities to keep the victim safe.\"\n\nCity Hall first leaned about the incident weeks ago when a tipster recognized Sutherland after watching the video posted on StopAntisemetism's social media accounts, said a source.\n\nThe same \"multicultural training\" Sutherland received will also now be mandatory for all Mayor's Office of Special Projects and Community Events staff to prevent similar hateful behavior in the future, said the City Hall source.\n\nSutherland is a \"junior staffer\" who doesn't directly communicate with Adams as part of her duties, added the source.\n\n\"Mayor Adams has been clear that hate has no place in our city, and the same - if not higher - standard should be held for our city's more than 300,000 employees,\" the Mayor's Office said.\n\n\"That is why disciplinary action was taken immediately after learning about this incident a few weeks ago.\"\n\n\"It is especially disturbing to learn that an individual employed by the mayor's office -- particularly in a position meant to celebrate the city's diversity -- is directly connected to this culture of hate,\" he said.",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/11/jews-ny-recognize-lululemon-adorned-94480993.jpg?quality=75&strip=all&w=1024",
            "eventUri": "eng-10133736",
            "sentiment": -0.1215686274509804,
            "wgt": 396,
            "relevance": 1
        },
        {
            "uri": "2024-11-557129797",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "06:15:52",
            "dateTime": "2024-11-26T06:15:52Z",
            "dateTimePub": "2024-11-26T06:12:36Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://indianexpress.com/article/india/26-11-mumbai-attack-president-murmu-leaders-pay-tribute-mumbai-terror-attack-martyrs-9690731/",
            "title": "26/11 Mumbai attack: President Murmu and leaders pay tribute to Mumbai terror attack victims on 16th anniversary",
            "body": "On the 16th anniversary of the 26/11 Mumbai terror attacks, President Droupadi Murmu on Tuesday paid tribute to the lives lost in the horrific attack that shook the nation.\n\nAdvertisement\n\nhttps://images.indianexpress.com/2020/08/1x1.png\n\n\"On the anniversary of the cowardly terror attacks in Mumbai on 26th November, 2008, I join the entire nation in paying homage to the bravehearts who lost their lives and expressing solidarity with their families,\" President Murmu said in a post on X.\n\nThe attack, carried out by 10 terrorists from Pakistan, remains one of the deadliest in India's history, claiming the lives of 166 people. While nine attackers were gunned down by Indian security forces, one surviving terrorist, Ajmal Kasab, was captured, tried, and later executed in November 2012.\n\nUttar Pradesh Chief Minister Yogi Adityanath also paid his respects to the victims of the attack, offering a heartfelt tribute to the lives lost. \"Humble tribute to the innocent citizens who lost their lives in the cowardly terror attack in Mumbai on 26/11 and heartfelt salute to the brave sons of Mother India who sacrificed their lives while performing their duties in this incident that tarnished humanity!\" Adityanath said in a post on X.\n\nAdvertisement\n\nHe further expressed his resolve to fight terrorism, stating, \"Let us be united and determined to end terrorism.\"\n\nMaharashtra Deputy Chief Ministers Devendra Fadnavis and Ajit Pawar, as well as the state's Governor C.P. Radhakrishnan, paid solemn tributes at the Martyrs Memorial in Mumbai, located on the premises of the Mumbai Police Commissioner's Office.\n\nIn a post on X, Union Home Minister Amit Shah condemned terrorism as \"a blot on the entire human civilization,\" while praising India's stance against such violence. \"The Modi government's 'zero tolerance' policy against terrorism has been appreciated by the entire world,\" Shah noted, saying that under this leadership, \"India has become a world leader in anti-terrorism initiatives.\"\n\nDefence Minister Rajnath Singh also took to X to mark the occasion, writing, \"We remember, and we will never forget those wounds,\".",
            "source": {
                "uri": "indianexpress.com",
                "dataType": "news",
                "title": "The Indian Express"
            },
            "authors": [],
            "image": "https://images.indianexpress.com/2023/11/2611-1-1.jpg",
            "eventUri": None,
            "sentiment": -0.615686274509804,
            "wgt": 391,
            "relevance": 1
        },
        {
            "uri": "2024-11-557859960",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "18:16:53",
            "dateTime": "2024-11-26T18:16:53Z",
            "dateTimePub": "2024-11-26T18:08:19Z",
            "dataType": "news",
            "sim": 0.7215686440467834,
            "url": "https://www.yahoo.com/news/israel-hezbollah-ceasefire-expected-halt-170404633.html",
            "title": "Israel-Hezbollah ceasefire expected to halt war in Lebanon within hours",
            "body": "Yahoo is using AI to generate takeaways from this article. This means the info may not always match what's in the article. Reporting mistakes helps us improve the experience.\n\nIsrael and the Iran-backed group Hezbollah appear set to halt the war that has killed almost 3,800 people in Lebanon over the last year and left about 16,000 others wounded. President Biden is expected to announce Tuesday that the U.S. helped secure a ceasefire in Lebanon, ending the fighting between Israel and Hezbollah, according to a U.S. official.\n\nUnder the deal, a full and permanent ceasefire would be implemented immediately. There will be 60 days permitted for the full withdrawal of Israeli forces -- a gradual withdrawal to allow the Lebanese forces to mobilize and move in to secure the area, but the trigger time is immediate, set to take effect later Tuesday.\n\nThe first peel-off of Israeli troops was to begin within the next 10 days.\n\nHezbollah is expected to pull its forces and heavy weapons back about 20 miles from the Israeli border, to the Litani River.\n\nAn official in Netanyahu's office told CBS News that the prime minister had convened the country's security cabinet to discuss the proposal. The cabinet must approve any ceasefire agreement. Netanyahu was also holding meetings Tuesday in Tel Aviv with various government ministers, lawmakers and mayors from some of the northern towns that have been evacuated for months.\n\nLebanon's government also had to unilaterally approve the deal on Tuesday, but the U.S. official said that was expected. The ceasefire would end the deadliest war in Lebanon since its civil war, which ended in 1990.\n\nNetanyahu was to address his country at 8 p.m. local time (1 p.m. Eastern) on Tuesday, according to his office, with Mr. Biden then delivering remarks about the agreement in Washington within a few hours.\n\nMr. Biden is expected to mention France when he speaks on Tuesday, according to a U.S. official. The French did not help negotiate the deal, but will be part of its implementation.\n\nPresident-elect Donald Trump's team has been briefed and looks upon the plan favorably, according to the U.S. official. Iran has also been briefed, given Tehran's support of Hezbollah -- a powerful military and political entity in Lebanon that has long been designated a terrorist group by both the U.S. and Israel.\n\n\"We are in the final stages of securing a ceasefire agreement for Lebanon,\" U.S. Secretary of State Antony Blinken told reporters Tuesday after meeting with G7 counterparts in Italy. \"We are not there yet, but I believe we are in the final stages.\"\n\n\"This has been an intensive diplomatic effort by the United States, partners like France working with Israel, working with Lebanon, over many months,\" Blinken said, \"and if we get to the conclusion that I hope we reach very soon, it will make a big difference. It will make a big difference in saving lives and livelihoods, in Lebanon and in Israel. It will make a big difference in creating the conditions that will allow people to return to their homes safely in northern Israel and in southern Lebanon.\"\n\nHezbollah started firing rockets into Israel on Oct. 8, 2023, in support of its Hamas allies who sparked the war in Gaza with their terror attack the previous day.\n\nIsrael carried out airstrikes on purported Hezbollah targets for months, but in September it dramatically escalated its assault on the Iranian proxy group, including by launching ground operations in the south of Lebanon.\n\nCBS News correspondent Debora Patta said rockets were still flying in both directions over Israel's northern border on Tuesday, with Israel and Hezbollah trading some of their heaviest fire to date, even as diplomats push for peace.\n\nUnder the proposed deal, Lebanese forces and United Nations peacekeepers are expected to jointly patrol southern Lebanon to ensure the terms of the agreement are adhered to. Earlier reports suggested the southern region would be monitored by a multi-nation committee, which would include both the U.S. and France.\n\nMiddle East expert Danny Citrinowicz, a fellow at the Atlantic Council think tank, said the deal looked \"good on paper,\" but added that until it was implemented, \"it would be hard to know whether Israel can really build on these kind of guarantees coming from the U.S. administration.\"\n\nAfter more than a year of crossfire, more than 1.2 million people have been displaced from their homes in Lebanon, along with at least 60,000 from towns and villages in northern Israel. They're all desperate to go home, and Israeli Prime Minister Benjamin Netanyahu has long said the chief objective of the war with Hezbollah, from his government's standpoint, has been to enable them to do so.\n\nWhile a deal with Hezbollah appeared closer than ever, negotiations for a ceasefire in Israel's war with Iran's other proxy force in the Gaza Strip, Hamas - have gone nowhere.\n\nBlinken said Tuesday that de-escalating tensions in the region \"can also help us to end the conflict in Gaza.\"\n\n\"In particular Hamas will know it can't count on other fronts opening up in the war,\" he said.\n\nMany in the decimated Palestinian territory are hungry, and recent rainstorms have made living conditions there even worse. A winter chill has set in, and there were reports of a fresh Israeli strike killing about 15 people Tuesday in Gaza City.\n\nLowrider cars celebrated as cultural symbol among Mexican Americans | 60 Minutes\n\nUATX says it fights college censorship culture with a focus on free speech | 60 Minutes",
            "source": {
                "uri": "yahoo.com",
                "dataType": "news",
                "title": "Yahoo"
            },
            "authors": [],
            "image": "https://s.yimg.com/ny/api/res/1.2/dxmyhn8AL.1zeGk_ZnGb0Q--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA-/https://media.zenfs.com/en/cbs_news_897/124cda88bc483090fb37eef630134a77",
            "eventUri": "eng-10120785",
            "sentiment": -0.1137254901960785,
            "wgt": 322,
            "relevance": 1
        },
        {
            "uri": "8449988056",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-09",
            "time": "21:25:03",
            "dateTime": "2024-12-09T21:25:03Z",
            "dateTimePub": "2024-12-09T21:21:03Z",
            "dataType": "news",
            "sim": 0.7176470756530762,
            "url": "https://freebeacon.com/campus/death-to-jews-inside-the-home-of-2-sjp-leaders-at-george-mason-university-police-find-guns-ammo-and-terrorist-flags/",
            "title": "'Death to Jews': Inside the Home of 2 SJP Leaders at George Mason University, Police Find Guns, Ammo, and Terrorist Flags",
            "body": "When police searched the home of two Students for Justice in Palestine leaders, a pair of sisters at George Mason University, their allies painted a sympathetic picture.\n\nThe students were targeted, according to the Council on American-Islamic Relations (CAIR), for engaging in \"anti-genocide events on campus.\" The Intercept reported that police found \"antique firearms\" registered to the students' brother and brought gun-related charges as a result of his family's \"pro-Palestine activism.\"\n\nExcluded from those descriptions was the crime the sisters are suspected of committing. A group of student radicals defaced George Mason's student center in August, spray painting messages that warned of a \"student intifada.\" In its coverage of the incident, the Washington Post wrote that \"activists spray-painted words on Wilkins Plaza outside the university's Johnson Center.\"\n\nThose activists caused thousands of dollars in damage, a felony in the state of Virginia, and police suspect the SJP leaders, sisters Jena and Noor Chanaa, led the group of vandals. Weeks after the incident, in November, a county judge granted a warrant -- which is under seal until February, according to a Fairfax County court representative -- allowing police to seize electronics from the Chanaa family home.\n\nWhen officers entered the Chanaa family home, they found firearms -- modern weapons, not antiques -- as well as scores of ammunition and foreign passports, all of which sat in plain view, according to court documents obtained by the Free Beacon and sources familiar with the investigation.\n\nThey also found pro-terror materials, including Hamas and Hezbollah flags and signs that read \"death to America\" and \"death to Jews,\" according to court documents and sources familiar.\n\nPolice seized the weapons under Virginia's red flag law, arguing that Mohammad Chanaa, the students' brother and a George Mason alumnus, was \"linked to destruction of property in connection with a large group of people with like-minded rhetoric\" and posed a danger to others given his possession of \"terroristic\" materials.\n\nOn the day of the search, Nov. 7, law enforcement officials removed \"long guns\" from the residence, sources say. A day later, Mohammad Chanaa voluntarily relinquished his 9mm handgun and concealed carry permit, according to court records. He was not charged with a crime -- Virginia's red flag law gives gun owners 14 days to petition a judge to return their firearms, and Mohammad Chanaa did so on Nov. 21. A Fairfax County circuit court judge granted his request as part of the civil case.\n\nCAIR has denounced the \"draconian measures used by law enforcement authorities\" to \"silence or intimidate those who seek to end the Israeli genocide in Gaza.\" A faculty group at George Mason, meanwhile, released a statement expressing \"deep concern about the apparent targeting of two George Mason students for their advocacy for Palestinian human rights.\"\n\nThe ongoing ordeal -- local police are investigating the incident with the FBI's assistance, sources familiar with that investigation tell the Free Beacon -- reflects CAIR and SJP's status as driving forces behind the anti-Semitic activism that has plagued college campuses in the wake of Hamas's Oct. 7 terror attack on Israel. It also reflects the radical, pro-terror views that have become synonymous with that activism.\n\nBoth Jena and Noor Chanaa have been deeply involved with George Mason's SJP chapter. Jena, a master's student studying civil and infrastructure engineering, served as the chapter's president last school year. Noor, an undergraduate student, took over as co-president this year. Their brother, Mohammad, is a recent George Mason graduate who served in the Springfield, Va., volunteer fire department as recently as Sept. 2023, records show. The three siblings hail from the area and live together in their parents' home.\n\nGeorge Mason did not respond to a request for comment. The FBI declined to comment. A spokeswoman for the Fairfax County commonwealth attorney's office, Laura Birnbaum, confirmed that officers found guns, ammunition, and pro-terror materials during their search and declined to comment further.\n\nThe Chanaa family attorney, Abdel-Rahman Hamed, did not respond to a request for comment. In a statement provided to the Washington Post, Hamed said the case marks \"yet another example of the police state targeting American Muslims without cause.\" An \"about\" section on his LinkedIn page states, \"I deny, defy, and defeat Zionists, antisemites, and White Supremacists.\"\n\nUnder Jena and Noor's leadership, George Mason's chapter of SJP has endorsed Hamas and its \"martyrs.\" In a statement issued two days after the Oct. 7 attack, the group lauded the \"liberation of the Palestinian people\" and endorsed \"the right to resist for Palestinians living under the zionist occupation.\" It said \"Palestinian resistance fighters\" mobilized \"into surrounding occupied areas\" on Oct. 7, \"reclaiming land and settlements considered illegal\" in the name of \"decolonization.\"\n\n\"Decolonization entails the struggle for liberation of a colonized people from the grasp of their colonizers,\" the statement read. \"This struggle for the much-sought after liberation from the colonizer is not meant to be metaphysical -- but material.\"\n\n\"Every Palestinian is a civilian even if they hold arms. A settler is an aggressor, a soldier, and an occupier even if they are lounging on our occupied beaches.\"\n\nThe group went on to hold campus protests rallying support for \"Palestinian martyrs\" and \"the resistance.\" On the one-year anniversary of Oct. 7, Jena Chanaa posted a photo of smiling Gazans on top of an Israeli military vehicle. \"One year ago we witnessed Gaza break through the prison doors. No cage will ever be strong enough to hold the colonized,\" she wrote in a caption. \"We have tasted liberation and will free ourselves in this lifetime. Glory to every single martyr in Gaza, Lebanon, and Yemen. May the earth burn for Gaza and may we avenge our martyrs every single day.\"\n\nMonths earlier, in a pair of Instagram posts, she wrote that her family comes from \"Taytaba in North Palestine\" and expressed a willingness to \"die in my homeland.\"\n\n\"76 years have passed since the forced expulsion of my family,\" she said. \"76 years of resistance to the occupation. 76 years of steadfastness and determination. 76 years of the complete belief that we will inevitably return.\"\n\nJena and Noor Chanaa and their associates appear to have leveled more aggressive threats toward their school through a pseudonym, using an Instagram account, \"gmuintifada.\" The account posted a video of the Aug. 30 vandalism the sisters are suspected of leading with the caption:\n\nWe, the George Mason University students of conscience, bear witness to the atrocities funded and supplied by our university, and we have chosen to retaliate. During the early hours of Wednesday morning, autonomous students left the imperial George Mason University a message: that the student intifada has been reignited, and that we will honor all the Gazan martyrs who did not live to witness this academic year. University administrations across the nation have convinced themselves that they can suffocate the flames of resistance that have been unleashed since the inception of this genocide. Yet, what they fail to realize is that their every effort to stifle our voices and eradicate our movement for liberation has only provoked an inferno that will engulf all systems of oppression that are upholding the genocide of the steadfast and honorable Palestinians. George Mason University, you will NEVER be able to escape accountability for your role in this genocide. Gaza is our compass and the heart of our noble struggle and the Student Intifada will confront every dousing of our eternal flame of resistance with precision. We will never be extinguished. Resistance until victory, GMU Intifada #escalate4gaza #studentintifada.\n\nShortly thereafter, George Mason police offered a $2,000 reward \"for information leading to the successful arrests of the persons involved in the criminal vandalism incident.\" The \"gmuintifada\" account has since been deleted from Instagram.\n\nIn the wake of the November search on the Chanaa home, George Mason slapped its SJP chapter with an interim suspension, according to a coalition of student groups affiliated with the chapter. University police also served Jena and Noor Chanaa \"with criminal trespass notices barring them from campus for four years,\" according to the Intercept.\n\nCAIR has called on George Mason to rescind those disciplinary measures.\n\nUniversity leaders see the case differently, with George Mason president Gregory Washington calling the school's actions \"justified based on the information available\" in a Nov. 20 faculty senate meeting. So do state and local law enforcement officials.\n\n\"For us at the state and local level, you know, we're concerned,\" one official told the Free Beacon, noting CAIR's ties to illicit fundraising efforts for Hamas as well as recent revelations that Iran has bankrolled anti-Israel campus protests in the United States.\n\n\"It clearly shows the connection between potential radicalization and some of these student groups that are out there,\" the official added. \"It needs to be investigated if these are just sympathies, or is there a road to radicalization?\"",
            "source": {
                "uri": "freebeacon.com",
                "dataType": "news",
                "title": "Washington Free Beacon"
            },
            "authors": [
                {
                    "uri": "collin_anderson@freebeacon.com",
                    "name": "Collin Anderson",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://freebeacon.com/wp-content/uploads/2024/12/george-mason.jpg",
            "eventUri": "eng-10159200",
            "sentiment": -0.1058823529411764,
            "wgt": 250,
            "relevance": 1
        },
        {
            "uri": "8429003539",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "04:13:00",
            "dateTime": "2024-11-26T04:13:00Z",
            "dateTimePub": "2024-11-26T04:12:25Z",
            "dataType": "news",
            "sim": 0.9490196108818054,
            "url": "https://nypost.com/2024/11/25/us-news/controversial-muslim-group-cair-forced-to-reveal-sources-of-funding-after-defamation-case-against-former-employee-backfires/",
            "title": "Exclusive | Controversial Muslim group CAIR forced to reveal sources of funding...",
            "body": "The Council on American-Islamic Relations (CAIR) will be forced to open its books and reveal its sources of funding after a defamation suit it filed against a former employee completely backfired.\n\nUS Magistrate Judge David Schultz ruled Monday that CAIR's donors, funding sources - including potentially foreign ones - and any assets owned by the group are all within the \"scope of permissible discovery\" as part of former chapter leader Lori Saroya's lawsuit against the controversial Muslim rights group.\n\nSaroya filed a federal defamation complaint against CAIR in January after the group dropped its own lawsuit against the former employee, which accused her of embarking on a \"defamation campaign\" against the organization, including by implying that CAIR is funded by foreign governments and terrorist organizations.\n\nCAIR alleged that Saroya's statements - posted on social media, in comment sections and emailed to the group's supporters - damaged the organization's ability to fundraise and build partnerships, but it ultimately dropped the lawsuit in January of 2022 over fears that Saroya's legal team would \"demand the names of CAIR supporters who have donated to us.\"\n\nJeffrey Robbins, Saroya's lawyer, described Monday's ruling as \"the mother of all legal boomerangs.\"\n\n\"It's a very important ruling,\" Robbins said of the Minnesota district court judge's order, in an interview with The Post, noting that the ruling is \"very methodical, very careful, very detailed and very analytical.\"\n\nRobbins explained that the order will force CAIR to \"turn over evidence about everything from fundraising practices, such as having raised money from foreign sources and concealed it; whether it deceived donors; whether it mismanaged donor money; whether it retaliated against employees or threatened to retaliate against employees for raising concerns about sexual harassment or the like.\"\n\nThe judge noted that \"the thrust of CAIR's allegations against Saroya in the 2021 complaint is that Saroya Falsely implied CAIR received funding from foreign governments and terrorists when she stated CAIR accepted 'international funding through their Washington Trust Foundation.'\"\n\nSchultz stated that \"CAIR points to no public admission that it received funding from terrorists or that it received funding through the Washington Trust Foundation\" but \"discovery into these matters is proportionate to the needs of the case.\"\n\n\"CAIR has not shown that the burden or expense of the proposed discovery outweighs its likely benefit, or that it unwarrantedly taxes its resources,\" he ruled.\n\nFormed in 1994 by a group of young Muslim activists concerned about the rise in anti-Muslim discrimination, CAIR is now the biggest Muslim civil rights group in the US and includes about 33 local chapters across the US.\n\nFederal tax filings show that CAIR received more than $5 million in grants and charitable contributions in both 2021 and 2022.\n\nAs a tax-exempt 501(3) nonprofit organization, CAIR is not typically required to reveal information about the identity of its donors.\n\nA September 2013 Department of Justice Office of Inspector General report on CAIR noted that evidence obtained during a 2008 federal case against the Holy Land Foundation for Relief and Development - a Muslim charity organization in the US found to have funneled millions of dollars to the Hamas terror group - \"linked CAIR leaders to Hamas, a specially designated terrorist organization, and CAIR was named as an unindicted co-conspirator in the case.\"\n\nCAIR officials have denied the DOJ OIG's claim.\n\nMore recently, the White House cut ties with CAIR last year after the group's co-founder, Nihad Awad, said he was \"happy\" to witness Hamas' terror attack against Israel on Oct 7.\n\nRobbins told The Post that he didn't want to speculate about what discovery disclosures would reveal about CAIR's funding sources but he said he expects the Minnesota federal court to issue a deadline for the group to fork over the names of its secret donors soon.\n\n\"We served requests that CAIR produce the documents that would show that what Ms. Saroya had said was true, and CAIR took the position that it should not have to turn over those documents,\" he said.\n\n\"So the ruling is almost across the board that CAIR does indeed have to turn over this evidence.\"\n\nSaroya is seeking at least $75,000 in compensation from CAIR and an injunction forcing the group to retract a January 2022 press release which allegedly defames her.\n\nCAIR did not respond to The Post's request for comment.",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/11/newspress-collage-23hlt0cyk-1732592105837.jpg?quality=75&strip=all&1732574149&w=1024",
            "eventUri": "eng-10120582",
            "sentiment": -0.1372549019607843,
            "wgt": 238,
            "relevance": 1
        },
        {
            "uri": "8447479141",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-08",
            "time": "05:02:49",
            "dateTime": "2024-12-08T05:02:49Z",
            "dateTimePub": "2024-12-08T05:02:35Z",
            "dataType": "news",
            "sim": 0.5372549295425415,
            "url": "https://www.breitbart.com/middle-east/2024/12/07/report-syrian-regime-falls-assad-flees-possible-plane-crash/",
            "title": "Report: Syrian Regime Falls; Assad Flees; Possible Plane Crash",
            "body": "Reports from the Middle East indicate that the Syrian regime of Bashar al-Assad has fallen, with the dictator fleeing the country as rebel forces entered the capital city of Damascus.\n\nUnconfirmed social media reports also suggest that Assad's plane crashed.\n\nThe sudden collapse of the Assad regime, dating back over half a century to the rule of Hafez al-Assad, Bashar's father, has rocked the Middle East and could mean the Iranian regime, a Syrian ally, is in danger.\n\nAssad was one of the most notorious tyrants in the world, one who used chemical weapons against his own people. His regime nearly fell in the civil war that erupted during the Arab Spring in 2011, but he was shored up by Russian and Iranian forces.\n\nPresident Vladimir Putin used Syria to restore Russia's presence in the Middle East for the first time since the Cold War, while Iran used Syria as a conduit to Hezbollah in Lebanon, sending weapons and advisers.\n\nAssad had bombed rebel-held cities with no regard for civilian life, and torturing suspected rebels and dissidents. President Barack Obama drew a \"red line\" in 2012 when he said the U.S. would intervene militarily if Assad used chemical weapons, but then failed to act.\n\nPresident Donald Trump launched airstrikes against the regime in 2017 after a chemical weapons attack, firing nearly 60 cruise missiles at Syrian air bases, which had the intended effect.\n\nTrump reduced the U.S. troop presence in Syria, though small forces remained to counter threats from the so-called \"Islamic State,\" or ISIS, which still operated in the country. Turkey also had an interest in Syria, targeting Kurdish militias operating in Syrian territory.\n\nBut Assad remained in power, thanks to Russia and Iran. Iran used Hezbollah forces from Lebanon to defend the regime, and they were accused of carrying out atrocities against Sunni regions.\n\nThe Syrian rebels -- including radical Islamist forces affiliated with Al Qaeda -- remained relatively weak. But the Third Lebanon War, which Hezbollah started by firing at Israeli cities after the Hamas terror attack of October 7, 2023, saw Hezbollah weakened and its supply lines disrupted.\n\nIn the wake of the ceasefire in Lebanon, the Syrian rebels, emboldened by Hezbollah's apparent defeat, began making rapid advances, meeting with little resistance.\n\nRussia, tied down by the war in Ukraine, was apparently unable (or unwilling) to intervene. Iran reportedly sent new military advisers, but also evacuated Iranian militias and personnel from the country.\n\nAssad was reported to have pulled his forces back to Damascus for a last stand, but there were reports of defections from his army as the rebels approached. The rebels appear to have used social media successfully to project strength and encourage surrender.\n\nThere were concerns about the fate of Assad's chemical weapons stockpile, which a deal brokered by Obama was supposed to have eliminated (but did not). There were unconfirmed reports that Israel had recently attacked a chemical weapons depot in Syria in an attempt to prevent the materials from falling into rebel hands. The rebels, according to social media reports, have claimed they will not use such weapons; their credibility is uncertain at best.\n\nThere are also concerns about the fate of religious minorities in Syria, particularly Christians. Israel has taken steps to reinforce its military presence on the Syrian border, warning the rebels not to attack it. President-elect Donald Trump said Saturday that the U.S. should stay out of Syria, and the Biden administration said it has no plans to intervene.\n\nFor now, the world waits to learn Assad's fate; to see who Syria's new rulers will be; and to see whether Iran is next.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/12/Syria-regime-falls-Associated-Press-e1733630430251.jpg",
            "eventUri": "eng-10151373",
            "sentiment": -0.592156862745098,
            "wgt": 227,
            "relevance": 1
        },
        {
            "uri": "2024-11-555350438",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-24",
            "time": "09:27:18",
            "dateTime": "2024-11-24T09:27:18Z",
            "dateTimePub": "2024-11-24T09:26:31Z",
            "dataType": "news",
            "sim": 0.7098039388656616,
            "url": "https://www.timesofisrael.com/body-of-slain-chabad-rabbi-found-in-uae-israel-condemns-antisemitic-act-of-terror/",
            "title": "Body of slain Chabad rabbi found in UAE; Israel condemns 'antisemitic act of terror'",
            "body": "Emirati authorities have found the body of Rabbi Zvi Kogan, an emissary to Abu Dhabi's Chabad chapter missing since Thursday, the Prime Minister's Office and Foreign Ministry said in a joint statement Sunday.\n\nIsrael's embassy in Abu Dhabi has been in contact with Kogan's family in the UAE, the statement said, and family members living Israel have also been updated.\n\nThe statement called the killing of Kogan \"a despicable antisemitic act of terror\" and pledged that Israel would use all available means to bring the killers to justice.\n\nThe Ynet news site reported that Kogan's car was found abandoned in Al Ain, around 150 kilometers (93 miles) from Abu Dhabi, where Kogan was based. It added, without citing sources, that there were signs of a struggle in the vehicle.\n\nOfficials suspect a number of Uzbek citizens recruited by Iran assaulted the rabbi and later fled to Turkey, the report said.\n\nAn unnamed official close to UAE authorities told Channel 12 that the country was angry and in shock, adding that senior state and religious officials were investigating.\n\n\"It happened after years when there wasn't an unusual security or nationalistic incident,\" the official was quoted as saying.\n\nKogan had been missing and presumed dead since Thursday.\n\nLawmakers and ministers in Israel released a flood of statements Sunday grieving his death and vowing a response to the murder.\n\nPresident Isaac Herzog said he mourned \"with sorrow and outrage,\" adding in a post on X: \"This vile antisemitic attack is a reminder of the inhumanity of the enemies of the Jewish people.\n\n\"It will not deter us from continuing to grow flourishing communities in the UAE or anywhere - especially with the help of the dedicated commitment and work of the Chabad emissaries all over the world.\"\n\nHerzog also thanked UAE authorities for their \"swift action,\" and said he trusted they will do all they can to bring the killers to justice.\n\nForeign Minister Israel Katz wrote on X that \"Israel will not rest nor be silent until those responsible for this criminal act pay for their actions.\"\n\n\"The State of Israel mourns the death of Rabbi Zvi Kogan,\" Opposition Leader Yair Lapid wrote on X, calling the killing an \"antisemitic terror incident\" and vowing that the UAE and Israel would cooperate in the investigation.\n\nNational Unity chair Benny Gantz also shared his grief on X, vowing that Israel would act and that his \"death will not be in vain.\"\n\nFollowing the incident, the National Security Council reiterated its travel warning to the UAE, saying there remains a threat against Israelis and Jews in the country.\n\nThe UAE has a Level 3 travel warning, the NSC said, meaning all nonessential travel should be avoided.\n\n\"Avoid visiting businesses, gathering places, and entertainment venues identified with the Israeli and Jewish population,\" the warning said. \"Maintain increased vigilance in public places (including restaurants, hotels, bars, etc.). Avoid displaying Israeli symbols. Cooperate with local security forces, follow their instructions, and report immediately if you have been exposed to terror activity.\"\n\nTravelers are also urged to avoid posting on social media and to lock their profiles online.\n\nKogan was a dual Israeli-Moldovan citizen, and has been part of the Abu Dhabi Chabad chapter since Israel normalized ties with the UAE in late 2020 under a US-brokered agreement dubbed the Abraham Accords. It has maintained the relationship throughout Israel's ongoing 13-month war in Gaza.\n\nAccording to Ynet, Kogan participated in the first ever Holocaust remembrance day ceremony in the Gulf state in 2021, and led the Yizkor prayer during the event.\n\nKogan is the nephew of Rabbi Gavriel Holtzberg, who was murdered along with his wife in a terror attack at the Nariman Chabad House in Mumbai in 2008.\n\nIsrael has been on high alert for Iranian efforts to harm Israelis and Jews around the world through its various agents and proxies, after the countries exchanged direct military blows for the first time this year.\n\nIran launched major drone and ballistic missile attacks against Israel in April and October, in response to Israeli strikes on its proxies in Lebanon and Syria. In late October, Israel retaliated with a series of strikes in which dozens of aircraft targeted strategic military sites across Iran as well as air defense batteries.\n\nIran has vowed to respond but has not yet done so in any major capacity.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [],
            "image": "https://static.timesofisrael.com/www/uploads/2024/11/zvi-fogel-e1732434964953.png",
            "eventUri": "eng-10112583",
            "sentiment": -0.4745098039215686,
            "wgt": 224,
            "relevance": 1
        },
        {
            "uri": "8467151702",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-20",
            "time": "19:33:04",
            "dateTime": "2024-12-20T19:33:04Z",
            "dateTimePub": "2024-12-20T19:32:25Z",
            "dataType": "news",
            "sim": 0.4901960790157318,
            "url": "https://nypost.com/2024/12/20/world-news/car-plows-into-people-at-german-christmas-market-leaving-several-injured-in-apparent-attack/",
            "title": "Several injured after car plows into crowd at German Christmas market...",
            "body": "A car plowed into a group of people shopping at a Christmas market in eastern Germany Friday -- leaving several people wounded in what officials are saying was a targeted attack.\n\nThe driver was immediately arrested after what local outlets are calling a terror attack in the city of Magdeburg, Bild reported.\n\nIt is not yet clear if anyone was killed in the mayhem.\n\nMagdeburg lies west of Berlin in the state capital of Saxony-Anhalt.",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/12/newspress-collage-1712ubosj-1734722667821.jpg?quality=75&strip=all&1734704698&w=1024",
            "eventUri": "eng-10192203",
            "sentiment": -0.6313725490196078,
            "wgt": 203,
            "relevance": 1
        },
        {
            "uri": "8453255431",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-11",
            "time": "19:18:51",
            "dateTime": "2024-12-11T19:18:51Z",
            "dateTimePub": "2024-12-11T19:18:20Z",
            "dataType": "news",
            "sim": 0.772549033164978,
            "url": "https://www.zerohedge.com/political/fbi-director-chris-wray-resigns",
            "title": "FBI Director Chris Wray Resigns",
            "body": "Before President-elect Donald Trump could say \"You're Fired!\" - FBI Director Christopher Wray has resigned, and will leave his post at the end of President Joe Biden's term.\n\nWhile Wray's departure was always in the cards, the move comes two days after Sen. Chuck Grassley (R-IA) wrote an 11-page letter to Wray asking him to step down, accusing him of mismanagement and \"failure to take control of the FBI.\"\n\n\"These failures are serious enough and their pattern widespread enough to have shattered my confidence in your leadership and the confidence and hope many others in Congress placed in you,\" wrote Grassley.\n\nAs the Epoch Times notes further, in November 2022, Grassley published FBI documents showing that higher-ranking officials were sometimes penalized less severely than subordinates.\n\nWray had addressed this disparity, saying in a Bureau-wide email on Dec. 11, 2020, that the agency \"has zero tolerance for any form of sexual harassment or sexual misconduct.\"\n\nOn March 4, 2022, FBI Deputy Director Abbate warned all FBI employees: \"Regardless of your rank and title, every one of us has the responsibility to treat everyone with dignity, respect, and professionalism. ... Harassment of any kind will not be tolerated.\"\n\nGrassley also mentioned in his letter his inquiry about the vetting of refugees from Afghanistan through the Operation Allies Welcome program. In February 2022, the Department of Justice (DOJ) reported that the Department of Homeland Security had not cross-checked these evacuees against data from the Department of Defense.\n\nAs a result, 50 individuals who had been flagged as \"potentially significant security concerns\" by the National Ground Intelligence Center were allowed into the United States.\n\nRequests to the FBI for further information were ignored, Grassley said.\n\nWray said \"in a classified multi-agency briefing to congressional staff\" that he was unsure of the location of other refugees who might pose a threat, Grassley wrote.\n\n\"I can't sit here right now and tell you that we know where all are located at any given time,\" Grassley quoted Wray as saying.\n\nHe pointed out that one potential terror threat had been foiled when the FBI arrested Nasir Ahmad Tawhedi on Oct. 7 of this year. Tawhedi was allegedly planning a terror attack to disrupt the U.S. election on Nov. 5.\n\nGrassley also accused Wray and the FBI of exercising a double standard by refusing to investigate President Joe Biden's or former Secretary of State Hillary Clinton's mishandling of classified information.\n\nPresident-elect Donald Trump appointed Wray in 2017 after firing the previous director, James Comey. In a recent interview with \"Meet the Press,\" Trump expressed displeasure over Wray's performance.\n\n\"He invaded my home,\" Trump said, referring to the 2022 FBI raid on his Florida residence, Mar-a-Lago.\n\nTrump also cited Wray's initial claim that his ear was struck by shrapnel instead of an assassin's bullet, and waning public respect for the FBI as an institution.\n\n\"I can't say I'm thrilled,\" he said.\n\n\"For the good of the country, it's time for you and your deputy to move on to the next chapter in your lives,\" the letter says.\n\nThe agency told The Epoch Times in an emailed statement: \"The FBI has repeatedly demonstrated our commitment to responding to Congressional oversight and being transparent with the American people.\n\n\"Director Wray and Deputy Director Abbate have taken strong actions toward achieving accountability in the areas mentioned in the letter and remain committed to sharing information about the continuously evolving threat environment facing our nation and the extraordinary work of the FBI.\"",
            "source": {
                "uri": "zerohedge.com",
                "dataType": "news",
                "title": "Zero Hedge"
            },
            "authors": [],
            "image": "https://assets.zerohedge.com/s3fs-public/styles/16_9_max_700/public/2024-12/chris%20wray1aa.jpg?itok=EpNdfZJQ",
            "eventUri": "eng-10158202",
            "sentiment": 0.003921568627450966,
            "wgt": 190,
            "relevance": 1
        },
        {
            "uri": "8466628887",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-20",
            "time": "12:39:53",
            "dateTime": "2024-12-20T12:39:53Z",
            "dateTimePub": "2024-12-20T12:38:33Z",
            "dataType": "news",
            "sim": 0.772549033164978,
            "url": "https://www.aljazeera.com/news/2024/12/20/israeli-settlers-set-mosque-on-fire-in-occupied-west-bank",
            "title": "Israeli settlers set mosque on fire in occupied West Bank",
            "body": "Governor of Salfit says the settlers had previously entered the village 'under the protection of the Israeli army'.\n\nIsraeli settlers have set fire to a mosque in the occupied West Bank, while also defacing the building's facade with hateful and racist slogans such as \"Revenge\" and \"Death to Arabs\" spray-painted in Hebrew.\n\nAbdallah Kamil, the governor of Salfit, said on Friday that the attack targeted the Bar al-Walidain mosque in the village of Marda, in the latest incident of settler violence.\n\n\"A group of settlers carried out an attack early this morning by setting fire to the mosque,\" Kamil said in a statement.\n\nOne resident of the village told AFP news agency that the settlers \"set fire to the entrance of the mosque and wrote Hebrew slogans on its walls\".\n\nAnother resident said the fire was extinguished before it could engulf the entire structure.\n\nNasfat al-Khufash, head of the Marda village council, also confirmed the \"systematic terror attack by a group of settlers\", in an interview with Reuters news agency.\n\nThe Israeli settlements on Palestinian land in the occupied West Bank are considered illegal by the United Nations and under international law.\n\nGovernor Kamil said that settlers had previously entered the village \"under the protection of the Israeli army\", and that similar acts of vandalism and graffiti had been reported in nearby areas.\n\nPalestine's Ministry of Foreign Affairs in Ramallah condemned the incident, calling it a \"blatant act of racism\" and a reflection of the \"widespread incitement campaigns against our people carried out by elements of the extremist right-wing ruling government\" of Israel.\n\nThe Israeli police and Shin Bet security services said in a joint statement: \"We see this incident as extremely serious and will act resolutely to bring the perpetrators to justice for rigorous trial.\"\n\nSettler violence in the illegally occupied West Bank has intensified since the war in Gaza began on October 7 last year. As of October 2024, there have been at least 1,400 settler attacks in the West Bank.\n\nSince the start of the war on Gaza, at least 803 Palestinians have been killed in the West Bank by Israeli forces or settlers, according to the Palestinian Health Ministry.",
            "source": {
                "uri": "aljazeera.com",
                "dataType": "news",
                "title": "Al Jazeera Online"
            },
            "authors": [],
            "image": "https://www.aljazeera.com/wp-content/uploads/2024/12/2024-12-20T100505Z_1028939150_RC2VSBAARJ06_RTRMADP_3_ISRAEL-PALESTINIANS-MOSQUE-SETTLERS-1734695816.jpg?resize=1920%2C1440",
            "eventUri": "eng-10190718",
            "sentiment": -0.4823529411764705,
            "wgt": 188,
            "relevance": 1
        },
        {
            "uri": "8430368642",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "20:53:50",
            "dateTime": "2024-11-26T20:53:50Z",
            "dateTimePub": "2024-11-26T20:53:23Z",
            "dataType": "news",
            "sim": 0.686274528503418,
            "url": "https://www.cnbc.com/2024/11/26/israel-lebanon-permanent-ceasefire-has-been-accepted-biden-says-.html",
            "title": "Israel-Lebanon permanent ceasefire has been accepted, Biden says",
            "body": "US President Joe Biden speaks about a ceasefire between Israel and Hezbollah in Lebanon, in the Rose Garden of the White House on November 26, 2024, in Washington, DC.\n\nIsrael and Lebanon's Hezbollah on Tuesday agreed to a permanent ceasefire in cross-border hostilities, following a year-long conflict between the Jewish state and Iranian-backed groups.\n\nPresident Joe Biden announced the deal, which was brokered by France and the U.S.\n\n\"Under the deal reached today, effective at 4:00 a.m. tomorrow, local time, the fighting across the Lebanese Israeli border will end,\" Biden said in the White House Rose Garden.\n\n\"This is designed to be a permanent cessation of hostilities,\" he added. \"What is left of Hezbollah and other terrorist organizations will not be allowed, I emphasize, will not be allowed, to threaten the security of Israel again.\"\n\nThe neighboring Middle Eastern countries have exchanged fire since October 2023, after Israel launched an expansive retaliatory military campaign in the Gaza Strip in response to a terror attack perpetrated by Palestinian militant group Hamas in the Jewish state.\n\nEarlier in the day Tuesday, Israeli Prime Minister Benjamin Netanyahu said in a televised address that he supported the ceasefire deal, which he sent to his Cabinet for approval.\n\n\"The ceasefire allows us to focus on the Iranian threat,\" said Netanyahu. \"We will complete the elimination of Hamas, the return of all the hostages and the return of the residents of the north.\"\n\nHezbollah has attributed its hostilities to solidarity with Palestinian civilians, while Israel has cited the right to self defense. The cross-border conflict has intensified since the summer, with Israel carrying out airstrikes that killed Hezbollah leader Hassan Nasrallah in late September, then proceeding with a ground invasion on Oct. 1.\n\nHostilities had continued on Tuesday amid the diplomatic overtures, with Israeli military spokesperson Avichay Adraee announcing the Jewish state was \"extensively\" attacking Hezbollah targets in Beirut in a Google-translated social media update.\n\nHezbollah, meanwhile, carried out missile strikes against an infantry training camp in Shavei Tzion in northern Israel, according to Hezbollah-aligned media outlet Al-Manar.\n\nSpeaking to the U.N. special envoy to Lebanon, Israeli Defense Minister Israel Katz called for \"effective enforcement\" from the U.N. if a ceasefire was implemented.\n\nHe warned in a Google-translated statement from his office that the Jewish state will \"act against any threat, anytime and anywhere\" and that \"every house in southern Lebanon that is rebuilt and in which a terrorist base is established will be demolished, every terrorist arming and organization will be attacked, every attempt to smuggle weapons will be thwarted, and every threat to our forces or Israeli citizens will be immediately destroyed.\"\n\nThe diplomatic breakthrough had been widely called for in the international community, which has repeatedly also urged for an end to offensives in the Gaza Strip to rein in the growing humanitarian crisis. Israel and Hamas previously honored a roughly week-long truce in November last year.\n\n\"On the proposal agreement brokered by the U.S. and France, Israel has all security concerns (addressed),\" the European Union's outgoing foreign policy chief Josep Borrell told reporters in Italy early on Tuesday, according to the Associated Press.\n\n\"There is not an excuse for not implementing a ceasefire. Otherwise, Lebanon will fall apart.\"",
            "source": {
                "uri": "cnbc.com",
                "dataType": "news",
                "title": "CNBC"
            },
            "authors": [
                {
                    "uri": "ruxandra_iordache@cnbc.com",
                    "name": "Ruxandra Iordache",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://image.cnbcfm.com/api/v1/image/108068507-1732653909925-gettyimages-2186367361-AFP_36NE2GB.jpeg?v=1732653946&w=1920&h=1080",
            "eventUri": "eng-10120785",
            "sentiment": -0.1137254901960785,
            "wgt": 171,
            "relevance": 1
        },
        {
            "uri": "2024-12-582509401",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-21",
            "time": "13:12:12",
            "dateTime": "2024-12-21T13:12:12Z",
            "dateTimePub": "2024-12-21T11:26:00Z",
            "dataType": "news",
            "sim": 0.5176470875740051,
            "url": "https://www.yahoo.com/news/germany-christmas-market-attack-latest-070051719.html",
            "title": "German Christmas market attack toll rises to 5 killed, 200 injured, minister says",
            "body": "FELIX FRANZ, EMILY SHAPIRO, AARON KATERSKY, MEREDITH DELISO, DAVID BRENNAN and VICTORIA BEAULE\n\nAt least five people are now known to have been killed in the vehicle-ramming attack on a Christmas market in the German city of Magdeburg on Friday, the Minister President of Saxony-Anhalt Reiner Haseloff told journalists on Saturday.\n\nHaseloff said that at least 200 more people were injured when a car plowed into festive market-goers in the eastern German city, around 75 miles west of the capital Berlin.\n\nA young child and an adult were among those killed in the attack, according to Haseloff. At least 40 of those injured were so seriously hurt that their lives are still thought to be in danger, according to a Chancellor Olaf Scholz.\n\nA suspect -- a doctor from Saudi Arabia aged around 50 -- was arrested, Haselhoff said. The man has lived in Germany since 2006. A rental car was used in the attack, the minister said.\n\nMORE: At least 2 dead, nearly 70 injured when car plows into German Christmas market: Officials\n\nThe motive is unknown at this time, U.S. sources said. But U.S. law enforcement sources told ABC News that German authorities are treating the attack as a terrorist incident.\n\n\"We send our deepest condolences to the families and loved ones of those killed and injured and to all those affected by this terrible incident,\" State Department spokesman Matthew Miller said in a statement.\n\n\"We stand in solidarity with the people of Germany in grieving the loss of life. The United States is ready to provide assistance as recovery efforts continue and authorities investigate this horrible incident,\" Miller's statement continued.\n\nScholz offered his condolences to those affected. \"My thoughts are with the victims and their families,\" Scholz said in a statement. \"We stand by their side and by the side of the people of Magdeburg. My thanks go to the dedicated rescue workers in these anxious hours.\"\n\nFriday's ramming incident came almost exactly eight years after a similar terror attack at a Christmas market in the German capital. On Dec. 19, 2016, a man drove a truck into a crowd at a market in Berlin, killing 13 and injuring dozens.\n\nU.S. law enforcement officials have warned of similar vehicle-ramming attacks on American soil, particularly over the festive season.\n\nA joint threat assessment about New Year's Eve in New York City's Times Square, for example, noted the use of vehicle-ramming alone or in conjunction with other tactics \"has become a recurring tactic employed by threat actors in the West.\"\n\nThe NYPD, out of an abundance of caution, will surge resources to similar areas around the city, including Christmas markets, according to NYPD deputy commissioner for counterterrorism Rebecca Weiner.\n\n\"We know this is a very festive time, it is a busy time in the city, and we are going to make sure that all of our holiday markets, all of our holiday activities are protected by our counter weapons teams, by officers on patrol, all our counter-terrorism officers, our critical response command,\" Weiner told ABC New York station WABC.",
            "source": {
                "uri": "yahoo.com",
                "dataType": "news",
                "title": "Yahoo"
            },
            "authors": [],
            "image": "https://s.yimg.com/ny/api/res/1.2/RCGcEe5zzsqxbX2Grd1lJw--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD02NzU-/https://media.zenfs.com/en/us.abcnews.gma.com/29eb69091530367a8354a9e6307337e2",
            "eventUri": "eng-10192203",
            "sentiment": -0.6,
            "wgt": 165,
            "relevance": 1
        },
        {
            "uri": "8468674815",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-22",
            "time": "04:09:35",
            "dateTime": "2024-12-22T04:09:35Z",
            "dateTimePub": "2024-12-22T04:09:09Z",
            "dataType": "news",
            "sim": 0.7568627595901489,
            "url": "https://www.foxnews.com/us/suspect-shot-killed-driving-truck-texas-mall-incident-left-least-5-injured-police",
            "title": "Suspect shot, killed after driving truck into Texas mall in incident that left at least 5 injured: police",
            "body": "Texas Department of Public Safety Sgt. Bryan Washko said that five people are injured and the suspect killed after he drove his car into the Killeen Mall in Texas on Saturday. (Credit: KWTX)\n\nAt least five people were injured, and a suspect was killed, after a man drove his pickup truck through the glass doors of a J.C. Penney in a mall in Texas, police said.\n\nThe incident happened on Saturday evening, just days before Christmas, at the Killeen Mall in Killeen, Texas - which is about 70 miles north of Austin.\n\nIn a press conference on Saturday evening, Texas Department of Public Safety Sgt. Bryan Washko said that the truck was driven \"several hundred yards\" through the entrance of the J.C. Penney store.\n\nStartled shoppers were injured as the driver was \"actively running people over\" and a fifth went to the hospital on their own, Sergeant Washko said. Those injured ranged from 6 to 75 years old, he said.\n\n5 DEAD, MANY INJURED AFTER MAN DRIVES INTO GERMAN CHRISTMAS MARKET IN SUSPECTED TERROR ATTACK: REPORT\n\nWATCH:\n\nThe incident unfolded as authorities noticed that the suspect, who has not been identified, was seen \"driving erratically,\" and police attempted to pull him over.\n\nCHILLING GOOGLE SEARCHES LEAD POLICE TO ARREST ACTIVE-DUTY MARINE IN ALLEGED MURDER OF ESCORT\n\nInstead of stopping, the driver got off the highway, drove to the parking lot of the Killeen Mall and smashed his car through the doors of the J.C. Penney, Sergeant Washko said.\n\nThe man driving the truck was fatally shot by law enforcement, authorities said.\n\nCLICK HERE TO GET THE FOX NEWS APP\n\n\"There were officers from D.P.S., the Killeen Police Department and three other agencies that engaged in gunfire to eliminate this threat to the community,\" Sergeant Washko said.\n\nFox News Digital has reached out to the Killeen Police Department for comment.",
            "source": {
                "uri": "foxnews.com",
                "dataType": "news",
                "title": "Fox News"
            },
            "authors": [
                {
                    "uri": "sarah_rumpf_whitten@foxnews.com",
                    "name": "Sarah Rumpf-Whitten",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2024/12/1024/512/8204d3c9-thumb.jpg?ve=1&tl=1",
            "eventUri": "eng-10194668",
            "sentiment": -0.3411764705882353,
            "wgt": 150,
            "relevance": 1
        },
        {
            "uri": "8462599156",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-18",
            "time": "03:40:36",
            "dateTime": "2024-12-18T03:40:36Z",
            "dateTimePub": "2024-12-18T03:39:39Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.breitbart.com/politics/2024/12/17/pro-palestinian-group-nyc-vows-support-armed-resistance-u-s-israel/",
            "title": "Pro-Palestinian Group in NYC Vows Support for Armed Resistance Against U.S., Israel",
            "body": "\"Our rifles will be pointed at the U.S. government and the Zionist entity,\" declared the speaker at a recent pro-Palestinian rally in New York, as he described American \"imperialists\" as the \"number one terrorists,\" and expressed solidarity with Hezbollah, a U.S.-designated terrorist organization, Iran, and other members of the \"Axis of Resistance.\"\n\nThe pro-Palestinian Bronx Anti-War Coalition, a self-described \"working-class, BIPOC-led, anti-imperialist\" group, organized a rally on Sunday in New York City's Union Square to express solidarity with the \"Axis of Resistance,\" which the group identified as Hezbollah, Iran, Syria, Yemen, and the Iraqi \"resistance.\"\n\nAt the event, a speaker donning a keffiyeh issued sharp proclamations, including: \"Stop pointing fingers at each other. Our fingers, our pens, our rifles will be pointed at the U.S. government, the Zionist entity, and nobody else.\"\n\nThe rally featured chants repeated by the crowd, calling out \"U.S. imperialists\" as the \"number one terrorists\" and voicing unity with regional terror movements.\n\nParticipants were seen waving flags representing the Palestinians; Iran, the leading state sponsor of terror; Iraq, where Iranian-backed militias hold significant influence; Lebanon, home to Hezbollah; Syria under Assad's regime, notorious for brutal crackdowns during its civil war; and Yemen, where the Houthi rebels align with Iran.\n\nThese were seen alongside Hezbollah's yellow flag, a known emblem of armed resistance and Islamic terror.\n\nHezbollah, which has actively sought to expand its influence beyond the Middle East, is designated a terrorist organization by more than a dozen countries and international entities, including major Western nations, members of the European Union, and most Arab League member states, due to its involvement in terrorist activities against American, French, Israeli, and other targets.\n\nFormer President Donald Trump has denounced Hezbollah, stating, \"No terrorist group other than al-Qaeda has more American blood on its hands.\" Meanwhile, Arkansas Republican Sen. Tom Cotton has called for the elimination of \"all of Hezbollah's leadership\" while insisting that the United States \"should let Israel win\" against Tehran's key terrorist proxy in the region.\n\nThe event also emphasized anti-sectarianism, with the speaker urging the crowd to \"rise above religious differences\" and focus on a shared cause.\n\nThe \"anti-capitalism\" Bronx Anti-War Coalition amplified their message on social media, sharing a video of Hamas spokesperson Abu Obeida denouncing sectarianism, as well as a speech by Hezbollah Secretary-General Naim Qassam streamed from Iran's Press TV.\n\nIn response, critics took to social media to express outrage over the rally's rhetoric.\n\n\"The day will come when these Palestine 'activists' inevitably execute a massive terror attack in NYC. And once they do, don't say we didn't warn you,\" wrote journalist Eitan Fischberger.\n\n\"Hey @RealTomHoman, here are some prime deportation candidates!\" wrote conservative commentator Dave Rubin.\n\n\"It's never been about Israel, it's always been about destroying Western civilization,\" wrote activist Eyal Yakoby.\n\nThe matter comes as the trend of anti-American sentiment at pro-Palestinian events continues to grow.\n\nAccording to world-renowned military historian and professor Dr. Victor Davis Hanson, Hamas's \"death cult\" relies on \"useful Western idiots\" to support the Palestinian cause, which has \"fused with the leftwing DEI industry.\"\n\nIn addition, he predicted over a year ago that pro-Palestinian protests and support for Hamas in the U.S. have alienated many Americans and would all but ensure a tough conservative president in 2024.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joshua_klein@breitbart.com",
                    "name": "Joshua Klein",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/12/nov29-2024-new-york-city-pro-palestinian-protest-getty.jpg",
            "eventUri": None,
            "sentiment": -0.3176470588235294,
            "wgt": 149,
            "relevance": 1
        },
        {
            "uri": "8458939061",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-15",
            "time": "19:03:02",
            "dateTime": "2024-12-15T19:03:02Z",
            "dateTimePub": "2024-12-15T19:01:58Z",
            "dataType": "news",
            "sim": 0.7568627595901489,
            "url": "https://www.breitbart.com/middle-east/2024/12/15/hamas-official-october-7-ruined-us/",
            "title": "Hamas Official: 'October 7 Ruined Us'",
            "body": "A senior official within the Palestinian terrorist organization Hamas admitted to a Saudi media outlet that the October 7 terror attack caused the destruction of the organization because of the ferocity of Israel's response.\n\nIsrael Hayom reported Sunday:\n\nA senior Hamas official currently based in Turkey told Saudi media that the 37th anniversary of the terrorist organization's founding comes during a period of decline due to defeats in Gaza and the broader region.\n\nThe official disclosed, \"Hamas is suffering from a genuine leadership crisis. The Al-Aqsa Flood attack backfired on us, submerging us in a sea of blood and crises. The most recent blow was the fall of Bashar al-Assad's regime in Syria, with which Hamas had been attempting to rebuild relations.\"\n\nAccording to a report by the Saudi news site Elaph, the Syrian government has ordered Palestinian terrorist groups to shut down their offices, hand over their weapons, dismantle training camps, and leave Syria as soon as possible. The primary Palestinian group active in Syria has been the Islamic Jihad. In contrast, Hamas's political bureau left Syria earlier due to its support for Islamist rebels at the start of the Syrian civil war, which sparked a rift with Assad.\n\nIsrael Hayom also cited reporting that Palestinian terrorists in Syria fled to Iran, but may leave for other countries due to the fear of assassination (Israel is suspected of having killed Hamas leader Ismail Haniyeh in Tehran in July.)\n\nThere are also Hamas officials in Turkey, and some are in Qatar -- including some who reportedly returned there at the urging of the incoming Trump administration, solely for the purpose of negotiating a hotage deal by January 20.\n\nThe report that Hamas leaders are accepting that the October 7 terror attack was a strategic mistake is a reversal from past months, and suggests that Israel is succeeding in restoring a deterrent against its enemies.\n\nHowever, there are European nations who continue to reward Hamas, with Ireland the latest to join South Africa's \"genocide\" case against Israel at the International Court of Justice. Ireland, Spain, and Norway also recognized a Palestinian state.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/10/IMG_9042-e1729259455839.jpg",
            "eventUri": "eng-10183384",
            "sentiment": -0.4745098039215686,
            "wgt": 142,
            "relevance": 18
        },
        {
            "uri": "8440647043",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-03",
            "time": "16:33:54",
            "dateTime": "2024-12-03T16:33:54Z",
            "dateTimePub": "2024-12-03T16:33:25Z",
            "dataType": "news",
            "sim": 0.2862745225429535,
            "url": "https://www.foxnews.com/us/train-hero-alek-skarlatos-daniel-penny-trial-this-could-happen-you",
            "title": "Train hero Alek Skarlatos on Daniel Penny trial: 'This could happen to you'",
            "body": "EXCLUSIVE: The Oregon Army National Guard veteran who helped thwart a terror attack on a train from Amsterdam to Paris in 2015 is warning that New York Marine veteran Daniel Penny's manslaughter trial is concerning to anyone who thinks of themselves as \"someone who would step up.\"\n\nOregon House Rep.-elect Alek Skarlatos, who along with two friends and another good Samaritan disarmed and subdued the Moroccan terrorist Ayoub El Khazzani when he opened fire on a packed Thalys train, said he believes French self-defense law is more accommodating than in the Empire State.\n\n\"Do you want people to step up and try to do the right thing or not? I mean, if he, God forbid, is convicted, it's going to frighten a lot of people and blue states into inaction,\" he said.\n\nThe problem with blue states, he warned, is an apparent double standard where politicized prosecutors pick and choose winners and losers.\n\nDANIEL PENNY PROSECUTOR DANGLES RACE CARD AGAIN OVER DEFENSE OBJECTION DESPITE NO HATE CRIME CHARGES\n\n\"I think if you live in Oregon, Washington, California and New York, you are kind of concerned that something like this could happen to you, especially if you're someone who thinks of themself as someone who would step up,\" he told Fox News Digital. \"In our terrorist attack, for instance...it happened on a gun-free continent. I wasn't able to carry. We had to fight this guy by hand.\"\n\nSkarlatos sees a two-tiered justice system in Democratic strongholds. Penny remained at the scene, spoke with police and was not arrested until 11 days later, when the same Manhattan District Attorney's Office that prosecuted the controversial NY v. Trump case indicted Penny on manslaughter charges.\n\nDANIEL PENNY RETURNS TO COURT FOR CLOSING ARGUMENTS IN SUBWAY CHOKEHOLD TRIAL\n\nNo one deserves to die because they're having a mental health episode, but at the same time, no one should have to put up with a drug-addicted schizophrenic person threatening their lives.\n\n-- Oregon House Rep.-elect Alek Skarlatos\n\n\"Hunter Biden is being pardoned today as well,\" Skarlatos said. \"There's all sorts of double standards when it comes to how blue states and Democrat leadership enforce the law.\"\n\nHe also said he believes Penny acted with others in mind, stepping in to stop an apparent threat before it got out of hand.\n\n\"If you watched his interview with police after the fact, he thought that he did the right thing and the police had Neely in custody and everything was going to be fine,\" he said.\n\nDANIEL PENNY DEFENSE CALLS FORENSIC PATHOLOGIST TO WITNESS STAND: 'THE CHOKEHOLD DID NOT CAUSE THE DEATH'\n\nSkarlatos and childhood friends Air Force Staff Sgt. Spencer Stone and Anthony Sadler were on board a Paris-bound train on Aug. 21, 2015, when El Khazzani jumped out of the bathroom and opened fire.\n\nThe now-convicted terrorist had an AK-47 rifle, an automatic pistol, a box cutter and hundreds of rounds of ammunition. The rifle jammed and they wrestled the guns away. By then, El Khazzani had shot one passenger, seriously slashed Mark Moogalian, an American ex-pat who was living in France and was first to engage the gunman, and cut Stone multiple times.\n\n\"When we kind of got control of him and had him bent over kind of a table in the train car, he was still fighting to get away, and so I just told him, 'Stop resisting, stop resisting.' And he didn't. So I put the handgun to the back of his head and pulled the trigger. And the handgun turned out to be completely empty,\" he said.\n\nSkarlatos cracked him in the head with the butt of the rifle instead as Stone, who nearly lost his thumb, choked him out.\n\nThe former Oregon National Guard sniper said he was afraid to tell French authorities at first.\n\n\"I actually asked the American FBI, who interviewed us the next morning, if it was something that the French would have a problem with,\" he said. \"And they said, no, pretty much it's terrorism. They don't care. You can do whatever you want to terrorists in France. And so when the French federal police interviewed me later that same day, I told them about that.\"\n\nThe three childhood friends received the French Legion of Honor, France's highest award, in 2015. Skarlatos was also given the Army's Soldier's Medal in a ceremony at the Pentagon. Stone, who said later his medical training helped save the life of the fourth passenger who stepped in, Moogalian, received the Airman's Medal and Purple Heart.\n\nAll three were invited to the White House when they returned home. They later played themselves in the Clint Eastwood-directed movie based on their memoir, \"The 15:17 to Paris\" in 2018.\n\nDANIEL PENNY DEFENSE RESTS AS FINAL WITNESS REVEALS JORDAN NEELY HAD OPEN WARRANT, DEFENDANT DOESN'T TESTIFY\n\nPenny's case has received national attention since the 26-year-old veteran's arrest on manslaughter and criminally negligent homicide charges in May 2023.\n\nHe placed Jordan Neely, a 30-year-old homeless man with schizophrenia and synthetic marijuana in his system, in a headlock to stop a fear-inducing outburst on a Manhattan subway car.\n\nNeely had an active arrest warrant at the time, a history of violent attacks, and witnesses testified that they feared for their lives as Neely screamed about killing people and not being afraid to go back to jail.\n\nPenny's defense has argued that the restraint was a justified use of force and that it was not the sole factor in Neely's death. Prosecutors accuse Penny of taking the move too far.\n\nCLICK HERE TO GET THE FOX NEWS APP\n\nHe faces a maximum of 15 years in prison if convicted.\n\nSkarlatos was elected to the Oregon House of Representatives last month. Once he takes office, he said, he hopes to oppose restrictive gun control measures and ensure citizens have a chance to defend themselves.\n\n\"Word on the street is the Democrats are going to be bringing a lot of anti-gun bills, which is kind of my pet cause, so to speak, being a gun owner and surviving what we survived in France,\" he said.",
            "source": {
                "uri": "foxnews.com",
                "dataType": "news",
                "title": "Fox News"
            },
            "authors": [
                {
                    "uri": "michael_ruiz@foxnews.com",
                    "name": "Michael Ruiz",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2024/11/1024/512/penny-neely-split-inset.png?ve=1&tl=1",
            "eventUri": "eng-10141450",
            "sentiment": -0.3411764705882353,
            "wgt": 137,
            "relevance": 1
        },
        {
            "uri": "8448133009",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-08",
            "time": "16:25:30",
            "dateTime": "2024-12-08T16:25:30Z",
            "dateTimePub": "2024-12-08T16:25:00Z",
            "dataType": "news",
            "sim": 0.7215686440467834,
            "url": "https://www.foxnews.com/world/new-reports-claim-unrwa-works-terrorists-teaches-hate-agency-hits-back-critics",
            "title": "New reports claim UNRWA works with terrorists, teaches hate as agency hits back at critics",
            "body": "By entering your email and pushing continue, you are agreeing to Fox News' Terms of Use and Privacy Policy, which includes our Notice of Financial Incentive.\n\nFollowing numerous allegations and charges against the United Nations Relief and Works Agency for Palestine Refugees in the Near East (UNRWA) over its ties to terrorists with involvement in the Hamas terrorist massacre in Israel, the scandal-hit agency is facing new allegations of wrongdoing.\n\nU.N. Watch a Geneva-based NGO, has released parts of a 150-page dossier that Executive Director Hillel Neuer told Fox News Digital shows \"high-level UNRWA staff who are complicit with terrorists, who meet with them regularly.\"\n\nBefore presenting his documentation to the world, Neuer attempted to address it directly with UNRWA Commissioner-General Philippe Lazzarini. In a letter to Lazzarini, Neuer explained that Lazzarini's staff have previously complained that U.N. Watch did not submit its reports to UNRWA for comment prior to publishing. Neuer then recounted several attempts to meet personally with Lazzarini to discuss U.N. Watch's findings and explained that when it released its dossier, Lazzarini would be unable to \"claim... that we do not show you the evidence in advance.\"\n\nUN, ISRAEL AT ODDS OVER CAUSE OF DECLINE IN AID DELIVERIES: 'False NARRATIVES BY INTERNATIONAL COMMUNITY'\n\nNeuer's group then released photographs of senior UNRWA staff, including Lazzarini and former UNRWA Commissioner-General Pierre Krahenbuhl, meeting with alleged terror leaders. \"You wouldn't find these photos on [UNRWA officials'] own social media,\" he said. \"We found them our own ways, but they don't post them.\"\n\nNeuer pointed Fox News Digital to two undated photos showing Lazzarini meeting with groups that included members of terror organizations, including the Jihadi Islamic Movement, the Islamic Ansar League, and Hamas.\n\nIn another photo dating back to late 2014, multiple UNRWA regional directors met with senior Hamas member Ali Baraka. Neuer said, and reporting from Al Watan Voice confirms, that the UNRWA staff wanted to \"to congratulate [Baraka] on Hamas' anniversary.\"\n\nIn another instance, Neuer said he was able to find a photo and transcript from a February 2017 meeting between former UNRWA chief Pierre Krahenbuhl, Baraka, members of the Popular Front for the Liberation of Palestine (PFLP) and Palestinian Islamic Jihad (PIJ), and others. According to U.N. Watch, Krahenbuhl reportedly told the assembly that \"we are united, and no one can separate us.\"\n\nIn September 2024, the U.S. Department of Justice announced \"terrorism, murder conspiracy, and sanctions-evasion charges\" against Baraka and five other Hamas leaders for their roles in Hamas' Oct. 7, 2023, terror attack, which killed 40 Americans and over 1,000 others.\n\nUN ACCUSED OF DOWNPLAYING HAMAS TERRORISTS' USE OF GAZA HOSPITALS AS NEW REPORT IGNORES IMPORTANT DETAILS\n\nKrahenbuhl and his staff were investigated in 2019 for reports of \"sexual misconduct, nepotism, retaliation, discrimination and other abuses of authority.\" Krahenbuhl resigned from his position, but in April 2024 was named the head of the International Committee of the Red Cross (ICRC). Leading congressional voices requested that Secretary of State Antony Blinken and U.S. Agency for International Development Administrator Samantha Power \"persuade the ICRC to reconsider this appointment\" given Krahenbuhl's \"disastrous tenure\" as UNRWA commissioner-general.\n\nFox News Digital asked the ICRC about the photos of Krahenbuhl posing with terror leaders, and of congressional concern about his fitness for the position in the Red Cross. An spokesperson told Fox News Digital that the ICRC \"was not present in the meeting, so it cannot speak to the full context of the discussion.\"\n\nThey also stated that Krahenbuhl \"has demonstrated through his work at ICRC and his decades of humanitarian experience that he has one objective: to secure aid to civilians in conflict zones. Meeting with any group that controls access to civilians, is an essential part of the ICRC work and other humanitarian organizations in conflict zones.\"\n\nU.N. Watch's latest dossier also includes interviews of UNRWA students taken by local Palestinian film crews over a period of three weeks during the summer of 2024. In one interview, a 14-year-old former student of UNRWA's Ein Arik co-ed school said that his school taught him \"'to fight back and resist' so that 'Palestine will be liberated and our lands will return to us by the good grace of Allah.'\" The child later explains that the solution for Jerusalem is to \"kill the Jews. We get rid of the Jews.\"\n\nA second NGO, IMPACT-se has reported extensively on educational materials used in UNRWA schools for over two decades. In a Nov. 13 report, IMPACT-se names 12 high-ranking UNRWA principals, deputies, directors or deputy directors of training centers who held membership in either Hamas or PIJ. The report notes that nine of the 12 participated in the terror attack of Oct. 7, with \"some even serving as Nukhba operatives,\" members of the special forces units of Hamas. Two of the dual UNRWA- and Hamas-member principals headed schools \"under which Hamas tunnels were built.\"\n\nISRAELI PARLIAMENT BANS UNRWA OVER TERRORISM TIES, FACES INTERNATIONAL BACKLASH\n\nThe latest IMPACT-se review complements findings from March 2023 that two UNRWA schools headed by Hamas members had \"promote[d] violence and terrorism in self-created study material.\" Now, IMPACT-se has named three additional schools where Hamas operatives served as UNRWA staff. The NGO found that these schools promoted \"libels against and non-recognition of Israel\" and \"gratuitously insert[ed] content promoting hatred and violence against Israel into grammar exercises.\"\n\nIMPACT-se found that UNRWA schools are \"shamelessly flout[ing]\" UNESCO standards, which include \"peace-building, respect for non-Palestinian groups, and avoiding incitement to violence.\"\n\nThe group's report cites intelligence claiming that \"over 10% of the 510 [senior] employees in UNRWA's education system in the Gaza Strip,\" are members of PIJ or Hamas. UNRWA members are not allowed to be participants in terror groups designated by the U.N. Security Council. But as Neuer explained, \"The U.N. terror list is one of the thinnest lists in the world,\" because \"Russia and China can block any designation they don't like.\" Neuer said this means \"there's virtually no Palestinian groups\" on the list.\n\nFox News Digital reached out to UNRWA media officials on numerous occasions for its response to the contents of IMPACT-se's and U.N. Watch's dossiers, about allegations that UNRWA schools were not adhering to UNESCO standards, and about Lazzarini's refusal to meet with Neuer.\n\nBill Deere, director of the UNRWA representative office in Washington, told Fox News Digital, \"UNRWA Commissioner-General Philippe Lazzarini has cautioned the spread of disinformation against UNRWA,\" which he says \"is meant to create chaos and divert attention from the political aims to dismantle the Agency.\" Reiterating the content of a statement Lazzarini shared on X in the aftermath of Neuer's dossier being released, Deere said, \"UNRWA recommends before giving oxygen to accusations like these, double-check the source and question the intent to avoid becoming an echo chamber for disinformation and de facto the fueling of hate and putting other people's lives in danger.\"\n\nCLICK HERE TO GET THE FOX NEWS APP\n\nAddressing U.N. Watch's interviews with UNRWA students, he said, \"What they don't tell you is these children were filmed without the knowledge or permission of their parents,\" Deere said. \"The kids were isolated and asked a series of leading questions designed to elicit a response. This is beyond misleading, it's twisted and desperate.\"\n\nThe U.S. was among numerous countries to pause support to UNRWA in January after the initial proofs emerged of members' participation in the terror attack of Oct. 7. Congress has halted funding to UNRWA through March 2025.",
            "source": {
                "uri": "foxnews.com",
                "dataType": "news",
                "title": "Fox News"
            },
            "authors": [
                {
                    "uri": "beth_bailey@foxnews.com",
                    "name": "Beth Bailey",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2024/03/1024/512/Gaza-Split-Photo-3.jpg?ve=1&tl=1",
            "eventUri": "eng-10151370",
            "sentiment": -0.1607843137254902,
            "wgt": 130,
            "relevance": 34
        },
        {
            "uri": "2024-12-576698457",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-15",
            "time": "20:03:20",
            "dateTime": "2024-12-15T20:03:20Z",
            "dateTimePub": "2024-12-15T20:02:19Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.infowars.com/posts/dirty-bomb-or-nuclear-warhead-in-usa-drone-mystery-could-be-covert-operation-searching-for-device-east-coast-radiation-levels-spike",
            "title": "Dirty Bomb Or Nuclear Warhead In USA? Drone Mystery Could Be Covert Operation Searching For Device",
            "body": "Globalists desperate to disrupt Trump peace negotiations ahead of inauguration.\n\nAccording multiple Infowars sources as well as whistleblowers posting online, the mysterious fleets of drones being sighted around the United States in recent weeks may be searching for a nuclear weapon that has been smuggled into the country.\n\nThe CEO of Saxon Aerospace John Ferguson recently posted a viral TikTok video claiming he knows a person who had knowledge of an old \"nuclear warhead\" left over from Ukraine by Moscow after the 1991 collapse of the Soviet Union.\n\n\"I spoke to a gentleman a few months ago, who was trying to raise the alarm to the highest levels of our government...about this one particular nuclear warhead that he physically put his hands on...that was left over from Ukraine...and he knew this thing was headed towards the United States,\" Ferguson said.\n\nHe continued to assess that the drones being sighted on the East Coast are trying to look for radioactive materials, and pointed out the Biden administration is \"pushing to get into war with Russia,\" suggesting a nuke set off in the U.S. could be blamed on the Vladimir Putin-led nation.\n\nInfowars founder Alex Jones commented on the post, writing, \"The American's information below is 100% correct. But there is a catch. He is only 100% right about one component. I have been waiting over the last week until I think through the second and third order consequences of telling you what I know. Stand by for the information today. If you ever ignored my warnings in the past and later, wished you would have listened, you want to pay attention now...\"\n\nAfter top podcast host Joe Rogan said Ferguson's video is the first take on the drones that has him \"genuinely concerned,\" Jones replied, \"I have confirmed with my sources in USNORTHCOM that this is indeed the purported reason the drones are swarming the NJ/NY area. But there is a lot more to it. I am headed in to the office to shoot a report that will be released today.\"\n\nAs Ferguson's video exploded online, another thread caught the internet's eye as an 𝕏 user called JerseyFutures claiming to be an RF engineer, who has since deleted the account, also alleged the drones are American-made aircraft trying to detect the presence of nuclear radiation from miles away.\n\nThe post suggested the U.S. military drones may be looking for a \"dirty bomb\" around New York.\n\nMeanwhile, the Geiger Counter World Map, which is currently experiencing off and on server issues, has been showing concerning radiation counts on the East Coast.\n\nConfirming the drones are active in New York, Democrat NY Governor Kathy Hochul issued a statement on Saturday revealing the aircraft caused \"runways at Stewart Airfield\" to be \"shut down for approximately one hour,\" adding, \"This has gone too far.\"\n\nNow, with the chatter that Russia could be blamed in a scenario where a bomb from Ukraine was smuggled into the U.S., it's worth going back to 2022 statements from Russia warning a nuclear False flag could be carried out and blamed on the Kremlin.\n\nIn March 2022, Ukraine's Director of Institute for Safety Problems of Nuclear Power Plants (ISPNPP), Anatolii Nosovskyi, warned that looters allegedly stole radioactive isotopes that could be used to make a \"dirty bomb\" after Russia gained control over the Chernobyl monitoring lab.\n\nJust weeks prior to Nosovskyi's accusation, Russia's Ambassador to Iraq Elbrus Kutrashev said fears of Ukraine deploying a dirty bomb against Russia were a leading factor in the decision to invade Ukraine in the first place.\n\n\"Nuclear. [They planned to use] nuclear waste in a bomb, and attack Russia or Russian interests, or maybe a concentration of Russians,\" he said. \"This forced us to choose as a priority of our special operation in Ukraine taking control of the nuclear plant in Chernobyl. We accomplished this successfully at the beginning of the operation.\"\n\nAlex Jones' 2022 analysis:\n\nThe Western mainstream narrative at the time was that Putin allowed the materials to be stolen, which is unconfirmed, in order to engage in a \"False flag\" dirty bomb attack against Russia.\n\nMoscow has repeatedly warned Western nations about Kiev's alleged plans to use a \"dirty bomb\" in Ukraine to frame Russia.\n\nOf course, with the CIA and NATO using Ukraine as a proxy army, it is the West that would be behind the dirty bomb plot if Kiev was \"behind\" an attack.\n\nIn July of this year, United Kingdom Parliament Member Andrew Bridgen claimed NATO and other parties were planning a False flag attack on a European city by detonating a nuclear \"dirty bomb\" to be blamed on Russia and launch WWIII.\n\nIran could also be blamed for the attack, as Republican Congressman Jefferson Van Drew of New Jersey claimed earlier this month that the New Jersey drones are being launched from an Iranian \"mothership\" stationed off the East Coast of the United States.\n\nWith President-elect Donald Trump set to take office for his second term, is it possible the Deep State scheme to detonate a dirty bomb in Ukraine or Europe was altered to now take place in New York or Washington D.C. in order to disrupt his presidency?\n\nThe American political establishment could even try to take Trump out (again) and come in as the saviors, telling the public the drones were trying to keep them safe from the dirty bomb threat and promising retaliation on whoever they blame.\n\nRelated: Multiple Sources Now Confirm Infowars Reports Of Surface-To-Air Missiles Inside US To Target Trump Force One\n\nAmerica's wide-open borders sure would make it easy for nefarious actors to enter the country with a warhead and carry out a terror attack, especially if assisted by globalists inside the U.S. government.\n\nDr. Naomi Wolf warned the Infowars audience just last month that the desperate Deep State may soon launch a nuclear attack inside America in order to disrupt the incoming Trump administration.",
            "source": {
                "uri": "infowars.com",
                "dataType": "news",
                "title": "Infowars"
            },
            "authors": [],
            "image": "https://imagedelivery.net/aeJ6ID7yrMczwy3WKNnwxg/852916e0-0a94-4e0c-eb5f-fa4b29279a00/w=800,h=450",
            "eventUri": None,
            "sentiment": -0.1137254901960785,
            "wgt": 120,
            "relevance": 1
        },
        {
            "uri": "8467582377",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-21",
            "time": "05:22:58",
            "dateTime": "2024-12-21T05:22:58Z",
            "dateTimePub": "2024-12-21T05:22:30Z",
            "dataType": "news",
            "sim": 0.47843137383461,
            "url": "https://nypost.com/2024/12/21/world-news/germany-magdeburg-christmas-market-driver-taleb-a-identified-as-anti-islam-activist/",
            "title": "Saudi doctor who crashed into German Christmas market, killing at...",
            "body": "The Saudi doctor arrested for the depraved and deadly car attack on a Christmas market in Germany has been identified as an anti-Islam activist, according to reports.\n\nThe man -- Taleb A., according to a report from The Guardian -- fled to Germany as a Saudi Arabian refugee in 2006 and gained official refugee status in 2016.\n\nThe 50-year-old left his home country due to its Islamic government and settled in Bernburg, where he worked as a doctor and psychotherapist after receiving his permanent status, according to the Wall Street Journal.\n\nHe was prominent in the Saudi community in Germany as an anti-Islam and women's rights activist -- running a website and social media channels dedicated to those causes, the Journal reports.\n\nOn his website, he warned prospective refugees to eschew Germany due to what he perceived as the government's tolerance of radical Islam.\n\nThe man also posted pro-Israel content in the wake of the Oct. 7 terror attack and was a supporter of Germany's rightwing anti-immigration party AfD, the newspaper reported.\n\nIn social media posts days before the attack, the suspect criticized the German government, claiming it was promoting the European nation's Islamization, and also alleged authorities were censoring him because of his views, according to The Wall Street Journal.\n\nTaleb A. is accused of plowing his car through a crowded Christmas market in Madgeburg, injuring dozens and killing at least 2, including a small child, in what authorities are calling a suspected terror attack.\n\nPolice operations remain ongoing in Magdeburg and Bernburg, where the suspect lives, The Guardian reports.\n\nThe attack comes one day after the anniversary of the 2016 Berlin Christmas market attack that killed 12 people and injured 56 in the deadliest terror attack in German history.",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/12/95678427.jpg?quality=75&strip=all&w=1024",
            "eventUri": "eng-10192203",
            "sentiment": -0.1843137254901961,
            "wgt": 110,
            "relevance": 34
        },
        {
            "uri": "8465028258",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-19",
            "time": "13:04:29",
            "dateTime": "2024-12-19T13:04:29Z",
            "dateTimePub": "2024-12-19T13:04:11Z",
            "dataType": "news",
            "sim": 0.47843137383461,
            "url": "https://nypost.com/2024/12/19/us-news/biden-admin-universities-presided-over-astounding-failure-to-crack-down-on-antisemitism-after-oct-7-scathing-house-gop-report-finds/",
            "title": "Exclusive | Biden admin, universities failed to crack down on antisemitism in...",
            "body": "The Biden administration, top universities and medical institutions utterly failed to crack down on antisemitism that exploded in the wake of Hamas' Oct. 7, 2023, terror attack, according to a scathing House Republican report released Thursday, which laid bare \"systemic\" and \"astounding\" shortcomings.\n\nSix GOP-led House committees declared in a joint report that \"antisemitism has been allowed to fester unchecked\" due to \"a disturbing pattern of defensiveness and denial,\" according to a copy exclusively obtained by The Post.\n\n\"Across the nation, Jewish Americans have been harassed, assaulted, intimidated, and subjected to hostile environments -- violations that stand in stark contrast to America's fundamental values, including a foundational commitment to religious freedom for all,\" the 42-page report says.\n\n\"The failure of our federal government departments and agencies is astounding.\"\n\nThe outpouring of anti-Israel and anti-Jewish remarks and actions tested America's free speech precepts and the fact that hate speech is generally lawful in the United States, unless it amounts to harassment or is an aggravating factor in a criminal act such as assault.\n\nThe Republican-led report points out, however, that federal law generally prevents recipients of taxpayer funds from tolerating discrimination -- allowing a foothold to leverage recipients to stiffen policies on campuses and at medical settings should federal officials so choose.\n\nIn almost every case, institutions allegedly took almost no disciplinary action against alleged antisemites and made no changes to codes of conduct, and faced no loss of grants to stop the rapidly spreading Jew hatred.\n\nThe report focuses heavily on Columbia University and its recommendations urge federal agencies to use money to incentivize more stringent anti-discrimination policies -- and also proposes potential legislation to that effect.\n\n\"The executive branch should aggressively enforce Title VI [anti-discrimination rules] and hold schools accountable for their failures to protect students. Universities that fail to fulfill the obligations upon which their federal funding is predicated or whose actions make clear they are unfit stewards of taxpayer\n\ndollars should be treated accordingly,\" the Republican panels said.\n\nHigh-profile reports of antisemitism -- mirrored by anti-Palestinian incidents that also occurred, especially during rallies and counter-rallies over the Israeli invasion of the Gaza Strip -- was just the tip of the iceberg, according to the investigation.\n\nIn one alarming incident, a student overheard two health care providers at Columbia's medical school discussing whether or not to \"treat her because she was Israeli.\"\n\n\"She sat in the room for another 10 minutes until someone finally came to address her health needs As of mid-December 2024, representatives of Columbia University have not provided any information to the Committees as a part of this investigation beyond an October 2, 2024, response of basic platitudes.\"\n\nThe Ivy League school, which was the site of a large encampment that featured on its fringes multiple documented instances of anti-Jewish remarks against pro-Israel activists and Jewish students, also reneged on a vow to punish students accused of breaking the rules to protest against Israel.\n\n\"Columbia said the 22 students arrested for the criminal takeover of Hamilton Hall would face expulsion. Instead, the University lifted the students' interim suspensions after pushback from radical faculty, allowing 7 to graduate, restoring 11 to good standing, and leaving 3 with preexisting sanctions suspended and 1 on probation,\" the report said.\n\n\"Despite dozens of students being arrested for conduct related to Hamilton Hall and the encampment,\n\nor having faced discipline for other egregious antisemitic incidents; Columbia failed to expel students and issued final suspensions to only four students.\"\n\nSome of the anti-Israel protesters at Columbia were themselves Jewish and argued that the protest was not pervasively antisemitic -- despite reported instances.\n\nThe document says that, unexpectedly, \"many colleges handed down disparate disciplinary actions for Jewish students versus their antagonists -- the students who engaged in antisemitic behavior, encampments, and intimidating tactics such as campus checkpoints and tax-exempt organizations that enabled and funded violent campus protests.\"\n\nColumbia, for example, \"allowed a False narrative that Jewish students had perpetrated a 'chemical attack' at an anti-Israel rally to persist for months despite knowing it was False and that the students involved had merely sprayed novelty 'fart sprays.'\n\n\"In an apparent case of disparate treatment, the Jewish students responsible were given excessive year-and-a-half long suspensions, substantially longer than any suspension for antisemitic conduct violations,\" the report says.\n\n\"Columbia failed to correct the record despite requests from the Jewish community, even as anti-Israel students used the False narrative of a 'chemical attack' purportedly involving military-grade 'skunk spray' to demonize Jewish students and call for excluding Israelis.\n\n\"Columbia finally acknowledged that the incident was not a 'chemical attack' in August 2024, pursuant to a settlement with one of the Jewish students excessively disciplined, which also awarded the student $395,000 and modified the suspension to conditional disciplinary probation.\"\n\nAllegedly biased institutions such as Columbia University, the University of Southern California, UCLA, George Washington University, Harvard University, and Yale University pocketed $2.7 billion in federal funds just in fiscal year 2023, which concluded right before Hamas terrorists invaded the Jewish state and killed more than 1,200 people -- including 33 Americans, the report says.\n\nThe probe, which was launched after House Speaker Mike Johnson (R-La.) and other Republicans took a tour of the anti-Israel encampment at Columbia, touched on many federal agencies.\n\nThe State Department and Department of Homeland Security allegedly stonewalled records requests about the visa statuses of those harassing Jewish students with terror-infused tirades -- or else discovered that government money was being funneled to tax-exempt charities\n\n\"Rather than confronting the severity of the problem, many institutions have dismissed congressional and public criticism and abdicated responsibility for the hostile environments they have enabled,\" the report states.\n\n\"This refusal to acknowledge or address the issue has allowed antisemitism to take root and thrive in spaces that contravene the values of this great nation.\"",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/12/95574064.jpg?quality=75&strip=all&w=1024",
            "eventUri": "eng-10183923",
            "sentiment": -0.4980392156862745,
            "wgt": 105,
            "relevance": 1
        },
        {
            "uri": "8467496341",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-21",
            "time": "03:19:02",
            "dateTime": "2024-12-21T03:19:02Z",
            "dateTimePub": "2024-12-21T03:18:18Z",
            "dataType": "news",
            "sim": 0.7686274647712708,
            "url": "https://www.breitbart.com/the-media/2024/12/20/community-notes-slams-associated-press-car-drove-crowd-christmas-market/",
            "title": "AP Slammed for Saying Car Drove into Crowd at Christmas Market",
            "body": "The Associated Press (AP) was slammed by people on X and received a community note after saying that a car drove into a crowd at a Christmas market in Germany.\n\nIn a post on X, the AP shared an article with the title, \"At least 2 dead and 60 hurt after a car drives into a German Christmas market in a suspected attack.\"\n\n\"A car has driven into a group of people at a Christmas market in Germany,\" the AP wrote in its post on X.\n\nAs Breitbart News's Kurt Zindulka reported, a man, who is \"reportedly from Saudi Arabia\" drove a car through \"a crowd of people at a Christmas market\" in the city of Magdeburg.\n\nThe community notes for the AP's post on X explains:\n\n\"A car has driven\" implies the car drove itself, which is factually incorrect. A man from Saudi Arabia intentionally drove the car into the Christmas market as a terror attack.\n\nSeveral people responded to the AP's post on X, questioning \"who was driving the car\" and criticizing the establishment media for writing \"headlines like this\" instead of being honest.\n\n\"The media likes to write headlines like this because instead of being honest about the driver being a terrorist, they hope you may just think it's one of those evil Elon Musk self driving cars acting up again,\" another person wrote in a post on X.\n\n\"'A car has driven into a group of people' might be one of the best possible examples of how the media has worked tirelessly to ensure that its importance and influence collapse,\" Ian Miller, a writer with Outkick wrote.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "elizabeth_weibel@breitbart.com",
                    "name": "Elizabeth Weibel",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/12/Magdeburg-Germany-terrorist-attack-Christmas-market-car-12-20-24-getty.jpg",
            "eventUri": "eng-10193647",
            "sentiment": -0.01960784313725494,
            "wgt": 105,
            "relevance": 1
        },
        {
            "uri": "8467256310",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-20",
            "time": "21:24:07",
            "dateTime": "2024-12-20T21:24:07Z",
            "dateTimePub": "2024-12-20T21:23:32Z",
            "dataType": "news",
            "sim": 0.5254902243614197,
            "url": "https://townhall.com/tipsheet/mattvespa/2024/12/20/how-the-media-reacted-to-the-german-christmas-market-attack-was-tragically-predictable-n2649400",
            "title": "How the Media Reacted to the German Christmas Market Attack Was Tragically Predictable",
            "body": "It's sad, but this event was almost predictable. Europe is awash with radical Muslims who wish death upon infidels, and Germany allowed hordes of these people into their country. At a local Christmas market in Magdeburg, one man, a reported Saudi Arabian, plowed through a crowd, killing at least several people and wounding as many as 60-80 others. We don't have official numbers yet (via NYT) [WARNING: Some graphic images]:\n\nA driver rammed a vehicle into a Christmas market in the city of Magdeburg in central Germany on Friday evening, killing at least one person and wounding dozens of others, in what local officials said they suspected had been an attack.\n\nThe driver of the vehicle was arrested, according to local news reports.\n\nAt least of 68 people were wounded, 15 of them severely, said Michael Reif, the spokesman for the city of Magdeburg. Mr. Reif and a regional government spokesman, Matthias Schuppe, both said they suspected the episode had not been an accident, according to the German public broadcaster.\n\n\"This is a terrible event, especially now in the days leading up to Christmas,\" Reiner Haseloff, the governor of Saxony-Anhalt state, where Magdeburg is the capital, told the German wire service D.P.A.\n\nMore than 1,000 temporary Christmas markets pop up every year in Germany, and they have been the target of terrorists in the past. In 2016, an extremist rammed a truck into a crowd in Berlin, killing 13. Since then, the police have secured many Christmas markets with temporary barriers.\n\nIt's a terror attack, and the suspect isn't some \"driver.\" That's the shameful part that's being omitted. The headlines read as if this vehicle got a life of its own, like something out of Stephen King's Christine. It was a Muslim man who decided he wanted to commit an act of radical Islamic terrorism. It's not just this incident.\n\nWhen it comes to the Israeli-Palestinian conflict and similar events, where terrorists try to run over Jews at bus stations, the Associated Press, one of the worst offenders of this trend, acts as if no one drove the cars. The suspect was also known to German security forces.",
            "source": {
                "uri": "townhall.com",
                "dataType": "news",
                "title": "Townhall"
            },
            "authors": [
                {
                    "uri": "matt_vespa@townhall.com",
                    "name": "Matt Vespa",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.townhall.com/cdn/hodl/2017/353/b72d9d01-fcf0-4a48-ac30-8f4c33d20139.jpg",
            "eventUri": "eng-10192203",
            "sentiment": -0.4588235294117647,
            "wgt": 105,
            "relevance": 1
        },
        {
            "uri": "8438764638",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-02",
            "time": "14:27:51",
            "dateTime": "2024-12-02T14:27:51Z",
            "dateTimePub": "2024-12-02T14:26:56Z",
            "dataType": "news",
            "sim": 0.6823529601097107,
            "url": "https://www.breitbart.com/middle-east/2024/12/02/american-hostage-omer-neutra-confirmed-dead-murdered-october-7-body-in-gaza/",
            "title": "American Hostage Omer Neutra Confirmed Dead; Murdered October 7, Body in Gaza",
            "body": "The Israel Defense Forces (IDF) declared Monday that American-Israeli hostage Omer Neutra, who was thought to have been taken alive to Gaza, was in fact killed during the October 7 terror attack and his body abducted by Hamas.\n\nOmer, who was 21 years old when he was killed, immigrated to Israel and joined the IDF as a \"lone solder,\" a term referring to those who join the military without any immediate family in Israel. He rose to the rank of Captain in a tank platoon in the 77th Battalion, 7th Brigade. His tank was hit by rocket-propelled grenades (RPGs) and other explosives in the assault, and though he and the other soldiers fought the terrorists outside the tank, they were killed.\n\nIsraeli President Isaac Herzog issued a statement:\n\nOur hearts are with the Neutra family this morning, who, after more than a year of a determined, traumatic, and worldwide struggle, received the devastating news confirming the death of their beloved son, Captain Omer Maxim Neutra, who fell on October 7th, and his body abducted by terrorists into Gaza.\n\nOmer was born and raised in the United States and chose to make Aliyah to Israel, and enlist in the IDF to stand in the defense of our people. After a preparatory year with the Garin Tzabar program, he service as a tank platoon commander.\n\nOver the past year, we had the privilege of meeting his parents, Ronen and Orna, and his brother Daniel -- a strong family with extraordinary resilience, who have dedicated their lives since October 7th to doing everything in their power to bring Omer home. I extend my warmest embrace to them and to all the families of the hostages enduring this horrific ordeal.\n\nWe must fulfill the ultimate imperative: to return Omer, and all our abducted men and women - the living to their families, and the fallen and murdered to be laid to rest.\n\nNews of Neutra's death came a day after Hamas released footage of another American-Israeli hostage, Eden Alexander, who is thought to be alive.\n\nThe number of living American hostages is now thought to be three: Alexander, 21; Keith Siegel, 65; and Sagui Dekel-Chen, 35.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/12/Screen-Shot-2024-12-02-at-5.40.23-AM-e1733146877593.png",
            "eventUri": "eng-10135563",
            "sentiment": -0.2627450980392156,
            "wgt": 104,
            "relevance": 1
        },
        {
            "uri": "8425424143",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-23",
            "time": "13:26:52",
            "dateTime": "2024-11-23T13:26:52Z",
            "dateTimePub": "2024-11-23T13:26:22Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://nypost.com/2024/11/23/us-news/zionist-org-preps-list-of-foreign-pro-hamas-students-hoping-trump-will-deport-them/",
            "title": "Zionist org preps list of foreign pro-Hamas students, hoping Trump...",
            "body": "A Zionist organization is compiling names of foreign students on visas in the US who spewed anti-Israel bile at campus protests -- and is hoping President-elect Trump will give the haters a one-way ticket back home.\n\nSo far, the group, Betar, has about 30 names of students from nations such as Jordan, Syria, Egypt, Canada, and the United Kingdom currently enrolled in some of the nation's top universities, including Columbia, UPenn, Michigan, Syracuse, UCLA, The New School for Social Research, Carnegie Mellon, and George Washington University.\n\n\"We have started commencing lists of Jew-hating foreign nationals on visas who support Hamas,\" said Ross Glick, director of the US chapter of Betar.\n\nBetar has IDed the haters using a combination of facial recognition software and \"relationship database technology\" to weed out people who were busted at antisemitic campus protests over the last year.\n\n\"One of our issues is processing power, there is just so much video to work through,\" Glick said.\n\nBetar is already in contact with \"prospective\" Trump administration appointees in the Justice Department about how best to take action on those identified, Glick said.\n\nAmong those on the list is Momodou Taal, a British national and PhD candidate in Africana studies at Cornell University, who was suspended twice for participating in a pair of on-campus Palestinian protests, most recently in September. University officials initially told Taal that the latest incident would lead to his F-1 visa being revoked, Newsweek reported. The Ivy later backed down.\n\nWeeks after the Oct. 7 Hamas terror attack in Israel, Trump vowed to deport foreign students who chanted in support of radical Islamic terrorism. He reiterated that promise to donors in May.\n\n\"When I am president we will not allow our colleges to be taken over by violent radicals. If you come from another country and try to bring jihadism or anti-Americanism or anti-Semitism to our campuses we will immediately deport you. You'll be out of that school,\" Trump said at a rally that same month.\n\nSaid Glick: \"We are strongly supportive of the Trump Administration's plan to deport jihadis who seek to destroy America. Our campuses and our streets are filled with violent people who hate Jews and cannot co-exist with Western society.\"\n\nOn Wednesday, Glick was on Capitol Hill meeting with lawmakers including pro-Israel Sen. John Fetterman (D-PA). Glick was in town to protest a Senate vote on whether to initiate an arms embargo against Israel.\n\nGlick also met with aids to Republican Sens. Ted Cruz and James Lankford.\n\n\"They all gave me the thumbs up and told me how to follow up,\" Glick said.\n\nOn the legislative front, Staten Island Rep. Nicole Malliotakis introduced a bill in February -- the No Visas for Anti-Semitic Students Act -- that would \"revoke the visas of students who have engaged in antisemitic activities.\"\n\n\"Entering our country to attend one of our esteemed universities is a privilege, and foreign students who conduct antisemitic activity on our campuses should have their visas revoked,\" Malliotakis said. \"I'm pleased the Trump Administration plans to take immediate action to have these individuals removed.\"\n\nBetar doesn't shy away from controversy.\n\nThe organization is banned from Facebook, Instagram, and WhatsApp because of a joke it made about handing out beepers to members of a pro-Palestine group at the University of Pittsburgh, referring to Israel's targeted beeper bomb attack against Hezbollah terrorists in Lebanon.\n\nThe group takes its name from Betar fortress, a prominent location in the Jewish-Roman wars of the second century. Betar was founded in 1923 by Ze'ev Jabotinsky, a prominent early Zionist leader.",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/11/newspress-collage-xe8uj7mg6-1732368084399.jpg?quality=75&strip=all&1732350156&w=1024",
            "eventUri": None,
            "sentiment": 0.02745098039215677,
            "wgt": 98,
            "relevance": 1
        },
        {
            "uri": "8468699213",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-22",
            "time": "04:47:32",
            "dateTime": "2024-12-22T04:47:32Z",
            "dateTimePub": "2024-12-22T04:46:29Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.indiatoday.in/world/story/ex-muslims-claim-germany-magdeburg-christmas-market-attack-saudi-atheist-warn-of-taqiyyah-conspiracy-2653579-2024-12-22",
            "title": "Ex-Muslims claim Germany Christmas market attacker isn't ex-Muslim, warn of bigger plot",
            "body": "Taleb Al Abdulmohsen (R), the Christmas market attacker, is a Shia Muslim who fled Sunni-majority Saudi Arabia and sought asylum in Germany in 2006. (AFP Images)\n\nAn attacker ploughed a black BMW into a crowded Christmas market in the German town of Magdeburg, killing five people and injuring 200 others. As 100 of the critically injured were battling for their lives, information trickled in about the attacker, Taleb Al Abdulmohsen or Taleb Abdul Jawad. A 50-year-old Saudi Shia refugee, Taleb worked as a doctor and claimed to be an ex-Muslim atheist. The information didn't add up for many and a large section of ex-Muslims are claiming that Taleb wasn't an ex-Muslim at all, and it was a big conspiracy.\n\nThe ex-Muslims are claiming that Taleb was a Shia extremist who carefully nurtured this atheist image over the years to hoodwink everyone, using the concept and licence of taqiyyah to further his Islamist goals.\n\nTaleb's curious case has taken experts by surprise.\n\n\"After 25 years in this business you think nothing could surprise you any more. But a 50-year-old Saudi ex-Muslim who lives in East Germany, loves the AfD (Alternative for Germany) and wants to punish Germany for its tolerance towards Islamists -- that really wasn't on my radar,\" says Peter Neumann, a German terrorism expert.\n\n\"If anything, the Magdeburg attacker Taleb A was far right: a self-declared Islam-hating, ex-Muslim atheist, who despised German society not for being against Islam but facilitating its spread,\" says Neumann.\n\nIs Taleb really an ex-Muslim doctor backing the anti-immigration AfD and a fan of right-wing Tesla boss Elon Musk? Or is this what the attacker wants us to believe he is?\n\nWould it be an ex-Muslim or an Islamic extremist who would target a Christmas market, and in effect Christians, ex-Muslims are asking. They are also asking if Taleb had put on the ex-Muslim garb just to facilitate his asylum or was it part of some bigger devious plan.\n\nBut first let's understand who ex-Muslims are.\n\nA section of people leaving Islam prefer being termed ex-Muslim. Unlike religions like Christianity or Hinduism, Islam punishes apostacy by death.\n\nHundreds of thousands of people had to risk their lives, sever ties with family and leave their countries just because they chose to leave their faith -- Islam.\n\nSome of the biggest critics of Islam have now emerged from among the ex-Muslims, who have gone and questioned the clergy on certain religious practices. Ex-Muslims support one another and have built a big community, thanks to the anonymity and safety provided by the internet.\n\nMillions of ex-Muslims have renounced their faith clandestinely and live a double life even without letting close family members into this secret.\n\nFor Taleb, claiming to be an ex-Muslim might have helped.\n\nTaleb, the Christmas market attacker, is a Shia Muslim who fled Sunni-majority Saudi Arabia and sought asylum in Germany in 2006.\n\nThere were charges of terrorism, rape and smuggling girls from the Middle East to EU countries against Taleb in Saudi Arabia, according to reports.\n\nTaleb said he was an ex-Muslim atheist, a factor that could get him persecuted in Saudi Arabia. He was given refugee status in 2016.\n\nThere were dozens of people, including ex-Muslims, claiming that Taleb used the ex-Muslim tag to get asylum.\n\n\"Taleb Al Abdulmohsen is not an atheist. He is a Shia extremist. Just because a Muslim self identifies as an atheist or claims to have converted to Christianity doesn't mean it's the truth,\" said Mahyar Tousi, founder of Yousi TV, an online alternative news platform.\n\nDespite requests by Saudi Arabia for Taleb's extradition, Germany refused to hand him over to him, fearing for his wellbeing there. This, even as Taleb repeatedly kept attacking Germany and its police force on social media.\n\nGerman authorities didn't act despite being alerted by a woman that Taleb was threatening to carry out a terror attack.\n\nThat could all be because of the image he developed over the years in Germany. Even the big media were deceived by his guile.\n\nOn social media, Taleb Al Abdulmohsen regularly shared posts on anti-Islam themes and engaged with other ex-Muslims.\n\nIn 2019, the BBC featured him in a documentary titled 'Helping ex-Muslims flee the Gulf'. It focused on how a website set up by him was helping ex-Muslims \"flee persecution in their Gulf homelands\".\n\nIn the video, Taleb said how he, at times, worked for 16 hours a day to help ex-Muslims escape Middle East countries. He said 90% of the requests for help were from women.\n\n\"I am history's most aggressive critic of Islam. If you don't believe me, ask the Arabs,\" he told Germany's FAZ newspaper, highlighting his ex-Muslim credentials.\n\nThough he interacted with the mainstream media, he declined interview requests from Brother Rachid, a popular ex-Muslim Christian influencer, twice in 2018 and 2020.\n\nBrother Rachid has been interviewing ex-Muslims for two decades and is known to ask tough questions.\n\n\"Each time, he cited a temporary medical condition, claiming his face was swollen as the reason he could not appear,\" said the TV host and author.\n\nA section of ex-Muslims, including those who interacted with Taleb, alleged that the Saudi attacker used the atheist image to hide his nefarious actions.\n\n\"He acted ex-Muslim on the outside, while in DMs he threatened ex-Muslims, especially Saudi women who had fled,\" said Ali Utlu, a Germany-based ex-Muslim atheist.\n\nUtlu said that Taleb had also repeatedly attacked him \"because I wanted nothing more to do with him after 2018\" and that he blocked him on X in May.\n\nYasmine Mohammed, a Canada-born ex-Muslim activist and author, said she knew Taleb for years from online interactions, and he didn't seem \"stable\" to her.\n\n\"He [Taleb] obsessively went after an ex-Muslim Saudi woman. He wanted my help in 'exposing' her and turned aggressive when I wouldn't comply. Friends have shared with me that he was targeting other Saudi female activists as well,\" said Yasmine Mohammed, a Canada-born ex-Muslim activist and author.\n\n\"There is suspicion now that he was actually working with Saudi authorities to bring down Saudi female activists. And although I cannot confirm this obviously, I will say that this theory aligns with my experience and exchanges with him,\" added Yasmine.\n\nEx-Muslims like Yasmine are worried that the Christmas market attack might bring unwarranted scrutiny on ex-Muslims and make their path to asylum difficult.\n\nTaleb supported the Alternative for Germany (AfD), a far-right political party that has a tough anti-immigration stance. This, despite Taleb being a refugee and trying to get other ex-Muslims into Germany.\n\nThat Tayeb's use of the ex-Muslim tag could be part of a bigger conspiracy was voiced by people like Mahyar Tousi of Yousi TV who said it was a clear case of Islamic taqiyya or taqiyyah.\n\nIranian-German entrepreneur Maral Salmassi posted a video explainer trashing \"claims made by the German press\" that Taleb was an ex-Muslim atheist, a fan of the AfD and Tesla boss Elon Musk.\n\n\"While he may have spread this misinformation himself, it aligns with the practice of Taqqiye, an Islamic doctrine that permits lying and deception to advance Islamic objectives,\" claimed Salmassi in the video.\n\nBritannica explains taqiyya or taqiyyah as an Islamic practice of \"concealing one's faith and forgoing ordinary religious duties under threat of death or injury to oneself or one's fellow Muslims\". It says its basis is found in the Quran.\n\n\"It has since been practised mostly among minority groups, particularly those of the Shi'ite (Shia) branch,\" says Britannica.\n\nTaleb was a Shia Muslim.\n\nIt is possible, suggest the ex-Muslims, that Taleb was acting as a mole in their community all these years, and, as one of the last acts, launched the terror attack at the Magdeburg Christmas market in a bid to endanger the entire community.\n\nEx-Muslim influencer Brother Rachid gave another recent example where a Muslim had claimed to have converted to Christianity but the truth was revealed after his death.\n\n\"Abdul Shokoor Ezedi, an Afghan migrant, applied for asylum in the UK, claiming a False conversion to Christianity. He even underwent baptism to bolster his claim,\" said Rachid.\n\n\"After being granted asylum, he was implicated in multiple crimes, including sexual assaults and a chemical attack on a woman and her children,\" he said.\n\nEzedi's body was found in the Thames in February, weeks after the chemical attack.\n\n\"Following his death, it was revealed that a mosque held an Islamic funeral for him, casting further doubt on the authenticity of his claimed conversion,\" said Brother Rachid, adding, \"This doesn't mean that there are no real conversions.\"\n\nIt's not without reason that anti-terror expert Peter Neumann is surprised by the Magdeburg Christmas market attacker's profile. The case of Taleb Al Abdulmohsen or Taleb Abdul Jawad is a curious one. There is an image that Taleb has been projecting, which has been accepted by German officials but is being junked by ex-Muslims who knew him for years. Whatever the truth, it needs to be ascertained.",
            "source": {
                "uri": "indiatoday.in",
                "dataType": "news",
                "title": "India Today"
            },
            "authors": [],
            "image": "https://akm-img-a-in.tosshub.com/indiatoday/images/story/202412/ex-muslims-claim-germany-christmas-market-attacker-isnt-ex-muslim--warn-of-bigger-plot-223308227-16x9_0.png?VersionId=QTWjrVeB26YOSSNjsNueiS3RDz.3kzc0",
            "eventUri": None,
            "sentiment": -0.2862745098039216,
            "wgt": 93,
            "relevance": 18
        },
        {
            "uri": "2024-12-581082263",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-19",
            "time": "23:29:28",
            "dateTime": "2024-12-19T23:29:28Z",
            "dateTimePub": "2024-12-19T23:29:00Z",
            "dataType": "news",
            "sim": 0.8745098114013672,
            "url": "https://www.timesofisrael.com/fbi-arrests-man-for-plotting-mass-casualty-attack-against-israeli-consulate-in-nyc/",
            "title": "FBI arrests man for plotting mass casualty attack against Israeli consulate in NYC",
            "body": "NEW YORK -- The FBI has arrested a suspect for a planned mass casualty terror attack against the Israeli consulate in New York City, the consulate said on Thursday.\n\nThe suspect, Abdullah Ezzeldin Taha Mohamed Hassan, was an Egyptian national living in Falls Church, Virginia, who instructed an FBI informant to carry out the attack, according to a criminal complaint filed on Monday.\n\nHassan ran several social media accounts that supported ISIS, al-Qaeda and Hamas, and advocated for violence against Jews, the FBI said in the complaint filed in a federal court in Virginia.\n\nLocal police located Hassan after receiving a tip about one of Hassan's accounts on X. An undercover FBI asset then connected with Hassan on social media and secure messaging apps.\n\nHassan allegedly instructed the informant on how to join ISIS and shared jihadist propaganda, including a video that advocated for killing Jews.\n\nHe encouraged the informant to carry out an attack, sending him instructions on how to create a \"martyrdom video,\" the complaint said.\n\nThe suspect sent the informant bomb-making instructions and told the informant, who said he was in New York, to target a building representing Jews, later settling on the Israeli consulate. The bomb-making instructions allegedly included the suggestion that packing the explosive with 30 mm aluminum ball bearings, for shrapnel, \"will do the trick.\"\n\nHassan told the informant how to surveil the consulate and how to escape to ISIS territory after the attack, and also suggested he could \"lay havoc on them with an assault rifle\" instead of a bomb. He also told the informant to livestream the attack so Hassan could give the footage to ISIS.\n\nThe conversations took place last month and this month, the complaint said.\n\nHassan, who according to a court filing was arrested on December 17, is accused of crimes related to distributing information on explosives and weapons of mass destruction.\n\nOfir Akunis, Israeli's consul-general in New York, thanked US security services for thwarting the planned attack.\n\n\"This attempted attack by terror organizations is an attack on the sovereign soil of the State of Israel in its entirety,\" Akunis said in a Thursday statement to The Times of Israel.\" \"It's proof that terror knows no boundaries and that we must fight it everywhere and every time.\"\n\nThere was no immediate comment from the US Justice Department on the arrest.\n\nAuthorities have prevented other recent terror attacks against Jews in New York.\n\nIn September, a suspect was arrested in Canada while attempting to enter the US to attack a Jewish center in Brooklyn in support of ISIS.\n\nAnd In July, a neo-Nazi was indicted for planning mass casualty attacks against Jews in New York City by distributing poisoned candy to Jewish children.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [
                {
                    "uri": "getty_images@timesofisrael.com",
                    "name": "Getty Images",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://static-cdn.toi-media.com/www/uploads/2024/12/AFP__20231009__1726474446__v1__HighRes__NewYorkRallyHeldInSupportOfGazaAsIsraelAndHa-e1734647342695.jpg",
            "eventUri": "eng-10189659",
            "sentiment": -0.3725490196078431,
            "wgt": 91,
            "relevance": 1
        },
        {
            "uri": "8467219263",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-20",
            "time": "20:43:47",
            "dateTime": "2024-12-20T20:43:47Z",
            "dateTimePub": "2024-12-20T20:43:12Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.dailywire.com/news/driver-mows-down-dozens-in-suspected-terror-attack-on-german-christmas-market",
            "title": "Driver Mows Down Dozens In Suspected Terror Attack On German Christmas Market",
            "body": "The suspected attack appeared to be similar to a 2016 Islamic terror attack in Germany that happened around Christmas.\n\nDozens of casualties were reported after a car plowed into a large number of people at a Christmas market in the German city of Magdeburg on Friday night in what officials say is a likely terrorist attack.\n\nEmergency services reported that at least 60 to 80 people were injured in the attack. German newspaper BILD reported that at least 11 people had died from their injuries in the attack.\n\nBILD also reported that the attacker \"is said to be a man from Saudi Arabia born in 1974.\"\n\nThe suspected driver of the vehicle, which drove down a street that was completely packed with people, was arrested shortly after the attack, officials said.\n\nWARNING: The following videos contain graphic material.\n\nWhile there was no immediate word about the identity of the attacker or a possible motive, law enforcement officials throughout Europe are often on high alert for Islamic terrorist attacks, especially around Christian and Jewish holidays.\n\nCHECK OUT THE DAILY WIRE HOLIDAY GIFT GUIDE\n\nThe threats posed by Islamic terrorists around the world have surged following Hamas' October 7 terrorist attack in Israel last year.\n\nIn December 2016, an Islamic terrorist stole a semi-truck and drove into a crowd, killing a dozen and wounding more than 50.",
            "source": {
                "uri": "dailywire.com",
                "dataType": "news",
                "title": "The Daily Wire"
            },
            "authors": [],
            "image": "https://dw-wp-production.imgix.net/2024/12/GettyImages-2190150566.jpg?w=1200&h=800&ixlib=react-9.3.0",
            "eventUri": None,
            "sentiment": -0.7725490196078432,
            "wgt": 84,
            "relevance": 1
        },
        {
            "uri": "8426349862",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-24",
            "time": "09:14:41",
            "dateTime": "2024-11-24T09:14:41Z",
            "dateTimePub": "2024-11-24T09:14:22Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.foxnews.com/world/calls-us-do-more-antisemitic-acts-skyrocket-europe-enormously-painful",
            "title": "Calls for US to do more as antisemitic acts skyrocket in Europe: 'enormously painful'",
            "body": "By entering your email and pushing continue, you are agreeing to Fox News' Terms of Use and Privacy Policy, which includes our Notice of Financial Incentive.\n\nOn Nov. 7, an anti-Israel mob set out on a \"Jew hunt\" through the streets of Amsterdam following a soccer game against a visiting Israeli team in what Israeli President Isaac Herzog termed an 'antisemitic pogrom.'\n\nWhen the angry mob was done hunting down and violently assaulting Jews and Israelis, five victims were hospitalized. Rioters continued to protest following the attacks setting a tram aflame on Nov. 11 and intensifying the spotlight on antisemitism throughout Europe.\n\nRabbi Abraham Cooper, Associate Dean and Director of Global Social Action for the Simon Wiesenthal Center, told Fox News Digital that his organization \"put a travel advisory on Amsterdam in the immediate aftermath of what happened.\" Cooper explained that the Simon Wiesenthal Center only takes this action \"very rarely\" and after serious deliberation.\n\nTRAM SET ON FIRE AS AMSTERDAM RIOTS RAGE ON\n\n\"Theoretically,\" Cooper added, \"you can slap a travel advisory on almost every place in Western Europe.\" As Cooper explained, \"the establishment has never stepped forward in any really major way across Europe to safeguard their Jews and guarantee their rights and their religious freedoms.\"\n\nFollowing Hamas' Oct. 7 terror attack on Israel, there has been a staggering increase in antisemitism across Europe. In May, citing data from the World Zionist Organization, Ynetnews reported an 800% increase in antisemitic incidents in Sweden over the previous year, as well as a 680% increase in Spain, a 450% increase in the Netherlands, a 442% increase in the UK and a 433% increase in France.\n\nEvents in Amsterdam appeared to be a flashpoint for further hate. On Nov. 10, Belgian authorities arrested five individuals after calls appeared on social media for a \"Jew Hunt\" in the Jewish Quarter of Antwerp, according to the Jerusalem Post.\n\nIn Greece in mid-November, protests featuring pro-Palestinian activists became so volatile that the Israeli Foreign Affairs Ministry advised Israelis to avoid the Embassy and certain other areas and to remove identifying symbols, the Jerusalem Post reported. Far from the first anti-Israel demonstration in Greece, in June, nine Europeans were under consideration for deportation following \"disruptive anti-Israel demonstrations\" at the University of Athens School of Law.\n\nNETANYAHU CONDEMNS ANTISEMITIC POGROM IN AMSTERDAM, WARNS WORLD LEADERS ATTACKS WILL SPREAD IF DON'T ACT\n\nThe Jerusalem Post reported that an under-17 youth soccer team in Berlin was \"chased and assaulted\" on Nov. 7 by a knife- and stick-wielding crowd screaming, \"Free Palestine.\" The Times of Israel reported that fewer than two weeks later, the Berlin Chief of Police told Jewish and gay residents to \"be careful\" in neighborhoods with high populations of Arabs. \"Unfortunately, there are certain neighborhoods where there are mostly Arab people who also have sympathy for terrorist groups,\" she explained.\n\nThe expansion of at-risk groups in Berlin echoes the warning words of Holocaust survivor Simon Wiesenthal. As Cooper explained, his organization's founder readily emphasized, \"It often starts with the Jews. It never ends with the Jews.\"\n\nIn the atmosphere of tension and hate, Cooper noted that Jewish Europeans are engaging in \"conditioning and self-censorship,\" removing yarmulkes, or taking the Jewish \"chai\" symbols from their necklaces. Cooper said that it has \"probably been about 15 years since a Jewish person felt comfortable walking to synagogue wearing a kippah in Amsterdam.\"\n\nCooper's concerns are borne out by media reports. As one Dutch Jewish citizen told Ynetnews, Jews visiting the Netherlands should not wear identifying items or \"bring Israeli passports.\" The Times reported in October that many Irish Jews are likewise removing identifying symbols due to an environment of mistrust.\n\nIn France, Jewish citizens are removing mezuzahs from their doors, avoiding riding in Ubers, and even changing their names to protect themselves from being identified and targeted with hate when they receive deliveries, according to the Christian Science Monitor. In 2023, France recorded 1,676 antisemitic incidents, compared with 436 the prior year. About 1,200 French Jews began applications to emigrate to Israel in 2023, an increase of 430% from 2022.\n\nADDRESSING ANTISEMITISM SHOULD BE PRIORITY FOR EUROPE BEFORE RECOGNIZING PALESTINIAN STATE, LEADING RABBI SAYS\n\nAs Cooper explained, it is \"enormously painful to look across Europe and to see that they give their due deference one or two days a year to dead Jews. They still haven't figured out in Europe how to live and embrace and celebrate Jewish presence in their societies.\"\n\nWith increased hate in Europe possibly impacting Americans traveling overseas, Fox News Digital asked the U.S. State Department whether it would issue travel advisories warning Jewish Americans of antisemitism abroad.\n\n\"We take seriously our commitment to provide U.S. citizens with clear, timely, and reliable information about every country in the world so they can make informed travel decisions,\" a spokesperson said. \"We use standard formats for our Travel Advisories and Alerts to help U.S. citizens find and use important security information easily. We encourage U.S. citizens traveling overseas to enroll in the Smart Traveler Enrollment Program (STEP.state.gov) to receive important safety and security updates, and to make it easier for the U.S. embassy or consulate to contact them in an emergency.\"\n\nCLICK HERE TO GET THE FOX NEWS APP\n\nThe Netherlands' Level-Two State Department Travel Advisory, last updated in August, notes threats of terrorism, but provides no information about antisemitic hatred. Neither do advisories for France, the United Kingdom, Germany, Belgium, or Greece.\n\nCooper emphasized that the Simon Wiesenthal Center hopes the incoming Trump administration will \"take the fight against antisemitism globally to a new level,\" making it \"part and parcel of American foreign policy, especially in the Americas and in the international organizations for which we fork out billions of dollars every year.\"",
            "source": {
                "uri": "foxnews.com",
                "dataType": "news",
                "title": "Fox News"
            },
            "authors": [
                {
                    "uri": "beth_bailey@foxnews.com",
                    "name": "Beth Bailey",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2023/11/1024/512/GettyImages-1755811073.jpg?ve=1&tl=1",
            "eventUri": None,
            "sentiment": -0.1843137254901961,
            "wgt": 80,
            "relevance": 1
        },
        {
            "uri": "8442430715",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-04",
            "time": "17:27:32",
            "dateTime": "2024-12-04T17:27:32Z",
            "dateTimePub": "2024-12-04T17:27:10Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.breitbart.com/politics/2024/12/04/report-doge-should-target-20-billion-spent-on-the-united-nations/",
            "title": "Report: DOGE Should Target $20 Billion Spent on the United Nations",
            "body": "Elon Musk and Vivek Ramaswamy of the unofficial Department of Government Efficiency (DOGE) should target the $20 billion spent by U.S. taxpayers on the United Nations, which often acts directly against American interests.\n\nThree \"Annes\" -- Anne Bayefsky, Anne Herzberg, and Anne Herzog -- write at Fox News that Musk and Ramaswamy can kill two birds with one stone, saving money for taxpayers while also strengthening U.S. foreign policy.\n\nThey write:\n\nIn the search to eliminate waste and unaccountable spending, a $20 billion annual savings plan is immediately available to incoming President Trump's Department of Government Efficiency (DOGE): American taxpayer dollars flowing to the United Nations.\n\nEach year the U.S. provides nearly a quarter of the U.N.'s total expenses, including assessed or mandatory \"regular\" funding of more than $3 billion and voluntary contributions that have vacillated between $10 and $15 billion in each of the past two years. Taking into account in-kind support services, the total is likely even higher. U.N. demands and U.S. subsidies have ballooned, with U.S. payouts almost doubling over the last decade.\n\n...\n\nAt the heart of the U.N. financial structure lies the bad idea that the United States must pay for whatever abomination it votes against. Fans call it burden-sharing. We pay for what we don't like, and other countries help pay for our priorities. The truth is that the end product doesn't shake out on the plus side either for American national interests or taxpayer pocketbooks.\n\nRead the full article here.\n\nThe Biden-Harris administration restored funding to UN bodies that the Trump administration had withheld, like the UN Reliew and Works Agency (UNRWA), later linked to the October 7 terror attack.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/07/united-nations-artificial-intelligence-symbol-of-united-nations-is-displayed-main-gate-un-headqua.jpg",
            "eventUri": None,
            "sentiment": 0.1137254901960785,
            "wgt": 79,
            "relevance": 1
        },
        {
            "uri": "8445909304",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-06",
            "time": "20:14:49",
            "dateTime": "2024-12-06T20:14:49Z",
            "dateTimePub": "2024-12-06T20:14:30Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://taskandpurpose.com/news/uss-carney-combat-sailors/",
            "title": "Sailors on USS Carney recall tense night of combat in fierce Red Sea fight",
            "body": "Navy sailors were expecting a typical deployment in late 2023 when the USS Carney left Florida. Instead, they fought \"the most intense combat engagement by a U.S. Navy warship since World War II.\"\n\nThe crew of the USS Carney thought they were headed for a normal deployment, and by \"normal,\" at least some of the crew was thinking about fun off the boat. At least that's what Fire Controlman 2nd Class Kameron Miller, a Mk. 160 gun console technician on his first deployment, was thinking.\n\n\"I've only heard stories, but I expected to pull into ports and party a little bit,\" said Miller. \"That was not quite the case.\"\n\nIt was not.\n\nMiller and the Carney left Naval Station Mayport, Florida on Sept. 27. On Oct. 7, just as the crew was arriving in the Red Sea for duty with the 5th Fleet, Hamas fighters invaded Israel in a massive terror attack, killing over 1,000. Within days, the Carney was on the front line of a rapidly escalating combat.\n\n\"The XO told us flat out what the situation was, and what we could be facing,\" said Gunner's Mate 1st Class Charles Currie, a Mk. 45 gun technician. \"At that point the crew just started to get ready.\"\n\nHouthi rebels in Yemen, backed by Iranian hardware, began firing missiles and drones at civilian merchant ships in the Red Sea, in an attempt to choke the vital trade route. The Carney quickly found itself as the primary U.S. Navy ship standing in the way.\n\nOn October 19, the Houthis took aim at the Carney.\n\nThe Navy released new details this week of that fight, including comments from crew members like Miller who found their expectations of placid duty and fun port calls swept away by a cruise that, when finished, faced 51 engagements.\n\nThe Oct. 19 battle began so unexpectedly that one crew member was initially confused by the ship-wide announcement.\n\n\"We were in berthing and heard [an announcement over the ship's 1MC intercom system] 'clear the weatherdecks,' and I remember thinking, 'what does that mean? I've never heard that before,'\" said Fire Controlman (AEGIS) 2nd Class Justin Parker, a SPY radar technician assigned to Carney.\n\nImmediately after the announcement, Parker heard the sound of missiles being fired off the ship, as well as the destroyer's main 5-inch guns. All aboard understood what it meant -- there were no scheduled live fire drills.\n\n\"We had never done anything like this before -- we had only trained to it,\" recalled Currie. \"There was a lot of adrenaline going on. This was real-world now.\"\n\nThe Carney is an Arleigh Burke-class destroyer, the Navy's primary class of ships tasked with protecting fleets from air attack. With a crew of over 300, the ship is armed with machine guns, 5-inch cannons and as many as 90 anti-aircraft missiles, along with separate suites of weapons for anti-ship and anti-submarine operations.\n\nBy the end of what became a 10-hour standoff, Carney had shot down 15 drones and four land-attack cruise missiles, an engagement the Navy called \"the most intense combat engagement by a U.S. Navy warship since World War II.\"\n\nAs the fight began and the ship defended itself, sailors said they remained calm.\n\n\"As nervous as you get, it's not about you,\" said Ensign William Hinckley, the ship's legal officer. \"It's about keeping everybody else safe. Thinking about everybody else and not just yourself is crucial.\"\n\nOver the next five months, the Carney engaged a threat no U.S. ship had faced before: Anti-Ship Ballistic Missiles, massive rockets fired designed specifically to sink ships like the Carney.\n\n\"The Houthis are the first entity in the history of the world to use anti-ship ballistic missiles ever,\" Vice Adm. Brad Cooper told 60 Minutes in February. \"No one has ever used an anti-ship ballistic missile certainly against commercial shipping, much less against U.S. Navy ships.\"\n\nF/A-18 Super Hornets and E/A-18 Growlers from the USS Eisenhower also engaged the ASBM, but the crew of the Carney faced them knowing they were the target.\n\n\"The ASBM threat is very challenging. It's very dynamic and it's very fast,\" said Cmdr. Jeremy Robertson, commanding officer of USS Carney in May. \"Because of that, we have to have 100% confidence in my [Tactical Action Officers] and all of the watch teams and all of the systems that we have that are designed to detect that and make sure that the ship is protecting itself.\"\n\nOn Dec. 16, the Carney took out another 14 drones, according to reporting in The War Zone.\n\nLt. j.g. Haven Vickers, the anti-submarine warfare officer assigned to the Carney, said the crew knew what to do. \"Every single training experience we did before deployment - that's what we fell back on,\" Vickers said.\n\nThe Carney returned to Florida in May. Chief of Naval Operations Adm. Lisa Franchetti awarded the ship the Combat Action Ribbon (CAR), the first time a Navy crew has received the decoration since 1991 in the Gulf War.\n\n\"I could not be more proud of what the Carney team has done since September,\" said Franchetti. \"It has been eye-watering to watch; you truly are America's Warfighting Navy in action.\"\n\n\"It was probably one of the most rewarding experiences I'll ever have in my entire life,\" said Miller. \"It wasn't just about traveling the world; it was about saving people's lives and getting a job done.\"",
            "source": {
                "uri": "taskandpurpose.com",
                "dataType": "news",
                "title": "Task & Purpose"
            },
            "authors": [
                {
                    "uri": "matt_white@taskandpurpose.com",
                    "name": "Matt White",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://taskandpurpose.com/wp-content/uploads/2024/12/452589323_935863808571961_8509698147995448336_n-e1733513386798.jpg",
            "eventUri": None,
            "sentiment": -0.1215686274509804,
            "wgt": 78,
            "relevance": 1
        },
        {
            "uri": "8458700039",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-15",
            "time": "14:34:45",
            "dateTime": "2024-12-15T14:34:45Z",
            "dateTimePub": "2024-12-15T14:33:38Z",
            "dataType": "news",
            "sim": 0.686274528503418,
            "url": "https://www.breitbart.com/europe/2024/12/15/israel-closes-embassy-ireland/",
            "title": "Israel Closes Dublin Embassy After Ireland Joins South Africa's 'Genocide' Case",
            "body": "Israel's foreign minister, Gideon Sa'ar, announced Sunday that the country would be closing its embassy in Ireland, following that country's decision to join South Africa's \"genocide\" claim at the International Court of Justice (ICJ).\n\nSouth Africa has sued Israel at the ICJ, claiming that it is committing \"genocide\" in response to the October 7, 2023, attack by Hamas. South Africa's case has elements of classic antisemitism, including the argument that Jews do not have the right to defend themselves when attacked, and misquotes of the Bible and Jewish teachings to claim that Jews are quilty a unique and religiously-motivated evil. It does not even acknowledge Hamas's genocidal ideology.\n\nSouth Africa's case has failed to gain much traction, even before a sympathetic court that is biased against Israel. Nevertheless, the government decided last week to join South Africa's \"genocide\" case -- although critics noted it changed the definition of \"genocide\" in doing so. The Foundation for Defense of Democracies, for example, observed: \"Ireland will also urge the court to develop and use a broader definition of the term \"genocide.\"\n\nThe Times of Israel reported:\n\nForeign Minister Gideon Sa'ar announces he will be closing Israel's embassy in Ireland, citing the \"extreme anti-Israel policy of the Irish government.\"\n\n...\n\n\"The antisemitic actions and rhetoric that Ireland is taking against Israel are based on delegitimization and demonization of the Jewish state and on double standards,\" says Sa'ar in a statement. \"Ireland has crossed all red lines in its relationship with Israel. Israel will invest its resources in promoting bilateral relations with the countries of the world according to priorities that are also derived from the attitude of the various countries towards it.\"\n\nAt the same time, Sa'ar announces that Israel will open an embassy in Moldova, which already has an embassy in Israel. The opening is expected to occur in the next year, and Israel is beginning the process of finding a site and appointing an ambassador.\n\nIsrael had recalled its ambassador from Ireland in May after it joined Spain and Norway in recognizing a Palestinian state. Such a state does not physically exist; recognition effectively rewards Hamas for the October 7 terror attack.\n\nThere has long been sympathy for the Palestinian cause within the movement for Irish sovereignty over the entire island, including the six counties of Northern Ireland that are part of the United Kingdom. Both causes have also harbored terrorist elements. The difference is that the Irish Republican Army eventually agreed to stop violence; Hamas and the Palestinian cause have never ceased to use terrorism and refuse to accept the existence of Israel.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/12/Ireland-Palestinian-protest-Getty-e1734270401148.jpg",
            "eventUri": "eng-10175304",
            "sentiment": -0.01960784313725494,
            "wgt": 75,
            "relevance": 1
        },
        {
            "uri": "8446068711",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-06",
            "time": "23:26:48",
            "dateTime": "2024-12-06T23:26:48Z",
            "dateTimePub": "2024-12-06T23:26:38Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://forward.com/news/680626/project-esther-heritage-jewish-conspiracy-antisemitism/",
            "title": "Scoop: Internal Project Esther documents describe conspiracy of Jewish 'masterminds' seeking to dismantle Western values",
            "body": "The Heritage Foundation's Project Esther, a conservative plan to counter antisemitism, sees the problem as one in which a handful of \"masterminds\" including Jews like George Soros and Illinois Gov. JB Pritzker are seeking to \"dismantle Western democracies, values and culture,\" according to internal Heritage documents obtained by the Forward.\n\nThe documents, a pitch deck that Heritage used in trying to build support from Jewish foundations and other organizations, also outline several tactics the group plans to use to undermine a collection of anti-Zionist nonprofits and progressive groups that it refers to as the Hamas Support Network. The actions include identifying \"foreign members vulnerable to deportation\" and enlisting law enforcement to \"generate uncomfortable conditions\" for progressive activists.\n\nHeritage did not respond to an inquiry Friday about the presentation.\n\nThe think tank, which also produced the controversial Project 2025 blueprint for a second Trump administration, has struggled to attract Jewish supporters for its antisemitism plan, which appears to have been assembled by several evangelical Christian groups.\n\nProject Esther focuses exclusively on left-wing critics of Israel, ignoring the antisemitism problems from white supremacists and other far-right groups. James Carafano, who runs the Heritage Foundation's antisemitism task force, said in October that \"white supremacists are not my problem because white supremacists are not part of being conservative.\"\n\nThe promotional presentation includes two slides headlined \"antisemitism's ecosystem.\" One features a pyramid topped by a list of \"progressive 'elites' leading the way.\" In addition to Soros and his son Alex, who run the Open Society Foundations, it also includes the Pritzker family and the Marxist academic and author Angela Davis.\n\nGeorge Soros has funded a variety of progressive causes and long been a boogeyman among conservatives; Alex recently took over the family foundation. It's less clear why JB Pritzker, who was first elected governor of Illinois in 2018, was on the list, or his broader family -- his sister Penny, who served as a Commerce Secretary under President Barack Obama and a special envoy for Ukraine in the Biden administration, is on the board of Harvard University and has compared pro-Palestinian protesters at the school to the Klu Klux Klan.\n\nPolitico reported in May that Pritzker family members ran a foundation that funded groups, including Climate Justice Alliance, which had also participated in pro-Palestinian demonstrations. But subsequent reporting cast doubt on those ties..\n\n\"That's a completely False story,\" JB Pritzker said of the Politico article at the time. He also chided the Chicago City Council for calling for a ceasefire in Gaza early this year.\n\nPritzker's office did not respond to a request for comment Friday.\n\nHeritage also accused lesser-known individuals of leading the network, including Neville Singham, who The New York Times has described as a charismatic millionaire \"known as a socialist benefactor of far-left causes;\" and Manolo de los Santos, who runs a \"movement incubator\" in New York City.\n\nThe pitch deck draws lines from these figures to \"Backers,\" including foundations both large and small, like Tides, which helps individual donors funnel more than $1 billion to various liberal nonprofits; the Rockefeller Brothers Fund; and Wespac, a tiny charity that sponsors several of the most radical pro-Palestinian groups in the country (and whose board chair is Jewish. Activist movements like Antifa and Black Lives Matter are also included on that tier, below which are \"organizers,\" including the nonprofit groups Jewish Voice for Peace, Students for Justice in Palestine and Fight Back, the arm of a Chicago construction workers union.\n\nIn the presentation, the work of these leaders, funders and organizations is described as \"violent activity\" directed at Jews, including \"riots.\" One slide includes a photo of a violent 2017 demonstration in Paris.\n\nProject Esther's strategy to \"neutralize\" this network, according to the documents, includes six distinct \"lines of effort\" with different outcomes.\n\nThe version of the plan publicly released on the one-year anniversary of the Oct. 7 Hamas terror attack in Israel, had criticized American Jewish organizations for not taking the threat posed by the \"Hamas Support Network\" seriously enough. The pitch deck says that Heritage plans to \"conduct tailored outreach\" to Jews and identify \"key influencers\" who can help unify the community behind Heritage's strategy.\n\nReferring to the activist network as a \"cancer,\" the group also calls for passing legislation to counter it at the federal, state and local levels. One goal is to get groups designated as \"TSEs,\" an abbreviation for \"terrorism support entity,\" which can have severe legal consequences.\n\nPresident-elect Donald Trump has pledged to make fighting antisemitism a priority in his administration. He has suggested that he's open to at least some of the tactics referenced in Project Esther, including deporting international students who protest against Israel. And the project was assembled by a group that includes the America First Policy Institute, a think tank staffed by some of his top advisors.\n\nNo major Jewish organizations appear to have participated in drafting the plan, or publicly endorsed it since its release.",
            "source": {
                "uri": "forward.com",
                "dataType": "news",
                "title": "The Forward"
            },
            "authors": [
                {
                    "uri": "arno_rosenfeld@forward.com",
                    "name": "Arno Rosenfeld",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://forward.com/wp-content/uploads/2024/12/GettyImages-660708178-scaled.jpg?_t=1733527312",
            "eventUri": None,
            "sentiment": -0.04313725490196074,
            "wgt": 75,
            "relevance": 1
        },
        {
            "uri": "8426708710",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-24",
            "time": "15:01:27",
            "dateTime": "2024-11-24T15:01:27Z",
            "dateTimePub": "2024-11-24T14:59:30Z",
            "dataType": "news",
            "sim": 0.7176470756530762,
            "url": "https://www.breitbart.com/national-security/2024/11/24/rabbi-confirmed-murdered-in-uae-netanyahu-antisemitic-terrorism/",
            "title": "Rabbi Confirmed Murdered in UAE; Netanyahu: 'Antisemitic Terrorism'",
            "body": "Rabbi Tzvi Kogan, the assistant rabbi to the growing Jewish community in Abu Dhabi, in the United Arab Emirates, was confirmed dead Sunday morning, apparently murdered by three Iranian agents from Uzbekistan who fled to Turkey.\n\nThe Chabad organization confirmed his death and asked people to do a good deed -- a \"mitzvah\" -- in his memory.\n\nRabbi Kogan had been missing since Thursday. Israeli officials contacted his relatives on Friday. There was reportedly some frustration among Israeli officials with the slow pace of investigation by UAE authorities, especially since Rabbi Kogan's car -- evidently driven by his assailants -- had reportedly been stopped for speeding on the road to Oman.\n\nPrime Minister Benjamin Netanyahu's office issued a statement:\n\nThe UAE intelligence and security authorities have located the body of Zvi Kogan, who has been missing since Thursday, 21 November 2024.\n\nThe Israeli mission in Abu Dhabi has been in contact with the family from the start of the event and is continuing to assist it at this difficult time; his family in Israel has also been updated.\n\nThe murder of Zvi Kogan, of blessed memory, is an abhorrent act of antisemitic terrorism. The State of Israel will use all means and will deal with the criminals responsible for his death to the fullest extent of the law.\n\nIsraeli President Isaac Herzog added that the terrorist act \"will not deter us from continuing to grow flourishing communities in the UAE or anywhere -- especially with the help of the dedicated commitment and work of the Chabad emissaries all over the world.\"\n\nChabad Lubavitch is a Hasidic movement that performs outreach to Jews of all backgrounds, and has become synonymous with the presence of Jewish communities of any significant size, anywhere in the world.\n\nThe murder of Rabbi Kogan took place almost sixteen years to the day of an Islamist terror attack on the Chabad House in Mumbai, India. Rabbi Kogan was related to Rabbi Gavriel Holtzberg, who was killed in that attack, the Times of Israel reports.\n\nThe murder is also a significant blow to the UAE's image as a safe and tolerant country. And it marks Iran's return to purely antisemitic terror attacks, rather than attacks on Israel or Israelis.\n\nIsrael normalized relations with the UAE under the Abraham Accords in 2020. Since then, Jewish communities in Dubai and Abu Dhabi have flourished. The country's first synagogue recently opened at the Abrahamic Family House in Abu Dhabi.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/11/IMG_0838-e1732435569588.jpg",
            "eventUri": "eng-10112583",
            "sentiment": -0.388235294117647,
            "wgt": 74,
            "relevance": 1
        },
        {
            "uri": "8446049375",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-06",
            "time": "23:02:00",
            "dateTime": "2024-12-06T23:02:00Z",
            "dateTimePub": "2024-12-06T23:01:51Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://nypost.com/2024/12/06/us-news/students-at-columbia-university-launch-anti-israel-columbia-intifada-newspaper-outrageous/",
            "title": "Students at Columbia University launch anti-Israel 'Columbia...",
            "body": "An anti-Israel student club at Columbia University freely distributed a new hateful newspaper on campus Friday -- peddling antagonistic rhetoric calling Jews \"colonists\" and \"subjugators.\"\n\nWhile the Ivy League institution denounced the publication, the hate-fueled group Students for Justice in Palestine openly handed out its inaugural edition of \"The Columbia Intifada.\"\n\nThe group printed 1,000 copies of the rag, which contains about a half-dozen articles with titles including \"Zionist Peace Means Palestinian Blood,\" \"The Myth of the Two-State Solution\" and a handy \"Guide to Wheatpasting\" -- a method of vandalizing public surfaces with propaganda fliers or other messaging.\n\nAllowing such a publication to take root on campus is \"outrageous,\" said New York Congressman Mike Lawler, who represents voters in Rockland, Westchester, Putnam and Dutchess counties.\n\n\"If Columbia cannot protect Jewish students on their campus, they should lose federal funding and have their tax-exempt status revoked,\" the rep wrote in a post on X.\n\n\"And for those students here on a visa engaged in an \"intifada\" against American students of the Jewish faith? Deport them,\" he raged.\n\nColumbia itself denounced the newspaper's publication, including its unauthorized association with the school by name.\n\nThe university suspended the group last November for repeatedly violating school policies, including with its \"threatening rhetoric and intimidation.\"\n\n\"Using the Columbia name for a publication that glorifies violence and makes individuals in our community feel targeted in any way is a breach of our values,\" a school representative said in a statement to The Post on Friday.\n\n\"As we have said repeatedly, discrimination and promoting violence or terror is not acceptable and antithetical to what our community stands for. We are investigating this incident through our applicable offices and policies.\"\n\nThe hateful group's four-page spread includes no bylines or any information connecting the articles to their respective authors, nor is there any solicitation for outside perspectives or reactions from readers.\n\nThe only words on the front-page masthead is a quote from a poem by woke extremist scholar Sophia Armen, which reads, \"You, genocider -- who remembers you?\"\n\nThe publication and distribution of the anti-Israel newsletter rattled some Jewish students.\n\n\"When I see stuff like that, the title, 'Myth of the Two-State Solution,' these people don't want peace,\" said Brooke Chasalow, 20, a pre-med junior who spent the previous two years in Israel through the dual-degree Tel Aviv University-Columbia University program.\n\nChasalow, who described herself to The Post as \"moderate\" on the Middle East conflict, said the conflict between Israel and Palestine is complicated, and she criticized protesters such as those behind the new incendiary paper for trying to turn it into a \"black and white issue.\"\n\nShe added that the university should be monitoring for hateful language, including the headlines printed in the SJP newspaper.\n\n\"I don't think we should encourage that stuff,\" she said, adding, \"Free speech is a wonderful thing, but it's not 'any speech.' \"\n\nStill, she said, the paper was an improvement from the chaotic protests on campus last year.\n\n\"If they're going to put out newspapers, that's easier to ignore. They're not screaming, 'Globalize the intifada!' in my face,\" she said.\n\nBut another Columbia student who declined to give her name or age said she is \"supportive\" of the radical publication.\n\n\"I encourage the diversity of ideas in a school when we're being censored,\" she said without elaborating further.\n\nSome faculty members shared Chasalow's point of view.\n\nGil Zussman, a professor of electrical engineering at Columbia, lived in Israel during the Mideast's bloody second Intifada.\n\nTwo violent uprisings by Palestinians in Israel's recent history are known as the first Intifada (1987-1993) and the second Intifada (2000-2005), in which terrorists besieged the nation with violence, often including horrific attacks against innocent civilians, with the stated goal of bringing the Jewish state to its knees.\n\nThe Antidefamation League says slogans referencing Intifada \"call for indiscriminate violence against Israel, and potentially against Jews and Jewish institutions worldwide.\"\n\nZussman said the fact that copies of the newspaper were being handed out on campus Friday -- and being promoted on social media by an anti-Israel staff collective known as the Faculty and Staff for Justice in Palestine at Columbia, Barnard, and Teachers College -- was \"very concerning.\"\n\n\"During the second Intifada, over 100 suicide bombings took place in Israel, and numerous buses exploded, resulting in over 1,000 people murdered,\" he said.\n\nI lived in Israel through that horrible period. The fact that faculty imply that such violence could or should be imported to Columbia is extremely irresponsible.\"\n\nColumbia University has been one of the epicenters for disruptive and at times violent anti-Israel protests on campus since Israel's war with Palestinian Hamas terrorists started in October 2023 when the Islamic extremist group launched a horrific coordinated terror attack, killing 1,200 Israelis.",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/12/94886380.jpg?quality=75&strip=all&w=1024",
            "eventUri": None,
            "sentiment": -0.0117647058823529,
            "wgt": 72,
            "relevance": 1
        },
        {
            "uri": "8432231738",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-27",
            "time": "23:30:54",
            "dateTime": "2024-11-27T23:30:54Z",
            "dateTimePub": "2024-11-27T23:30:23Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.dailywire.com/news/former-human-rights-watch-exec-dismisses-hostages-of-hamas-as-utter-irrelevancies",
            "title": "Former Human Rights Watch Exec Dismisses Hostages Of Hamas As 'Utter Irrelevancies'",
            "body": "A former head of Human Rights Watch (HRW) described dozens of hostages held by Hamas as \"utter irrelevancies\" on Wednesday.\n\nKenneth Roth, a visiting professor at Princeton and the former executive director of HRW, accused the Israeli government of giving \"diversionary excuses\" in response to charges against two top officials by the International Criminal Court (ICC) in The Hague. The ICC charged Prime Minister Benjamin Netanyahu and his former defense minister, Yoav Gallant, of committing war crimes in the war against Hamas in Gaza.\n\nOne of the \"excuses\" cited by Roth is Israel's mission to rescue roughly 100 hostages taken by Hamas during its October 7, 2023, terror attack.\n\n\"The Israeli government responded to the ICC war-crime charges with the usual diversionary excuses - the need to liberate the hostages, Hamas's use of human shields, Israel's democracy and self-defense, supposed ICC antisemitism - all utter irrelevancies,\" Roth said in a post on X.\n\nIn a later post, Roth said that the ICC charges are not about whether Israel's war is just, but about \"HOW [Israel] is waging the war. Nothing justifies war crimes.\" But he also called for a ceasefire between Israel and Hamas, and said Israel's only reason for continuing the war in Gaza was Netanyahu's \"need for a forever war to retain power and avoid prison...\"\n\nRoth served as the executive director of HRC from 1993 to 2022. He received pushback online for his characterization of the hostages held by Hamas.\n\n\"I can think of 101 people, in addition to their families, who might argue that the hostages are not 'utterly irrelevant' to IDF operations in Gaza,\" Melissa Weiss, executive editor of Jewish Insider, wrote on X.\n\nInternational Legal Forum CEO Arsen Ostrovsky called Roth \"an absolute heartless monster.\"\n\nAdam Cannon, the director of legal at the British tabloid The Sun, said that Roth's post showcases the \"huge anti Israel bias\" as HRC.\n\nCannon wrote to Roth on X: \"Your dismissal of the Hamas atrocities and the hostage they took on Oct 7 just illustrates your total lack of understanding or maybe just abject bias when it comes to this conflict, undermining an organisation which should be at the forefront of helping solve the issues.\"",
            "source": {
                "uri": "dailywire.com",
                "dataType": "news",
                "title": "The Daily Wire"
            },
            "authors": [],
            "image": "https://dw-wp-production.imgix.net/2024/11/Kenneth-Roth.jpg?w=1200&h=800&ixlib=react-9.3.0",
            "eventUri": None,
            "sentiment": -0.4352941176470588,
            "wgt": 70,
            "relevance": 1
        },
        {
            "uri": "8449939069",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-09",
            "time": "20:31:52",
            "dateTime": "2024-12-09T20:31:52Z",
            "dateTimePub": "2024-12-09T20:30:08Z",
            "dataType": "news",
            "sim": 0.5490196347236633,
            "url": "https://www.breitbart.com/politics/2024/12/09/lebanese-christians-rejoice-freed-after-decades-in-assads-prisons/",
            "title": "Lebanese Christians Rejoice: Freed After Decades in Assad's Prisons",
            "body": "Christians in Lebanon are celebrating the release of several prisoners who were abducted by the Syrian regime over several decades of occupation and who are now, finally, free after the sudden collapse of the Assad regime on Sunday.\n\nL'Orient Today reported:\n\nSouheil Hamawi, a Lebanese national detained in Syria for 33 years, has returned to his home in North Lebanon. Hamawi, who claimed he was arrested in December 1992 at his home in Chekka, arrived in his village accompanied by a brass band and was welcomed by relatives in an emotional reunion, according to our correspondent Michel Hallak.\n\nIn an interview with local television, Hamawi recounted his ordeal, stating that he had been arrested when his son was just 10 months old. Now a grandfather, Hamawi expressed eagerness to meet his family after decades apart. He revealed that he had been transferred between several Syrian regime prisons before ending up in Latakia's coastal facility, where he was the only Lebanese detainee. For 15 years, his family had no information about his whereabouts, though they later managed to locate him and have occasional contact. Hamawi paid tribute to his wife for enduring what he described as significant hardships in his absence.\n\n...\n\nWhile reports circulate of other Lebanese detainees being released, only one other case has been confirmed: Ali Hassan al-Ali, a man from Akkar, who was freed from Hama prison last week. However, al-Ali has not yet returned to Lebanon, according to his family.\n\nSome of the missing Chistians were political activists; others were members of Christian militias that had been active during the Lebanese civil wars of the 20th century.\n\nSyria dominated Lebanon for decades until it was eclipsed by Iran and its proxy, Hezbollah, who propped up a faltering Assad regime while continuing to dominate Lebanese politics.\n\nMany commenters on social media are outraged at former Lebanese President Michel Aoun, a Christian, for taking Syrian dictator Bashar al-Assad at his word when the latter claimed that there were no more Lebanese prisoners in Syria.\n\nSome are praising Israeli Prime Minister Benjamin Netanyahu, whose leadership of Israel during the ongoing war that was started by Iranian proxies Hamas and Hezbollah last October ultimately resulted in the decimation of Hezbollah and the elimination of its leadership, leaving Assad defenseless.\n\nOthers faulted the Iranian regime itself, whose strategy of surrounding Israel with a \"ring of fire\" consisting of terrorist proxies ultimately failed with Hamas's decision to launch the brutal October 7 terror attack, which underestimated the strength of the Israeli response.\n\nWhile there is still widespread concern about the fate of Christians inside Syria, especially since the Syrian rebels who overthrew Assad are radical Islamists with ties to terror, there is broad delight at the demise of the Syrian regime.\n\nJoel B. Pollak is Senior Editor-at-Large at Breitbart News and the host of Breitbart News Sunday on Sirius XM Patriot on Sunday evenings from 7 p.m. to 10 p.m. ET (4 p.m. to 7 p.m. PT). He is the author of The Agenda: What Trump Should Do in His First 100 Days, available for pre-order on Amazon. He is also the author of The Trumpian Virtues: The Lessons and Legacy of Donald Trump's Presidency, now available on Audible. He is a winner of the 2018 Robert Novak Journalism Alumni Fellowship. Follow him on Twitter at @joelpollak.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/12/Freed-Lebanese-Christian-Getty-e1733770918798.jpg",
            "eventUri": "eng-10153247",
            "sentiment": -0.1137254901960785,
            "wgt": 69,
            "relevance": 1
        },
        {
            "uri": "2024-12-573418162",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-12",
            "time": "04:18:07",
            "dateTime": "2024-12-12T04:18:07Z",
            "dateTimePub": "2024-12-12T04:17:19Z",
            "dataType": "news",
            "sim": 0.7176470756530762,
            "url": "https://www.timesofisrael.com/syrian-rebel-chief-says-working-with-intl-groups-to-secure-potential-chemical-arms-sites/",
            "title": "Syrian rebel chief says working with int'l groups to secure potential chemical arms sites",
            "body": "Syrian rebel leader Ahmad al-Sharaa, better known as Abu Mohammed al-Golani, told Reuters Wednesday that the jihadist group he leads, Hayat Tahrir al-Sham (HTS), is working with international organizations to secure possible sites where chemical weapons may be located.\n\nHTS, which is rooted in al-Qaeda's Syria branch but has in recent years sought to moderate its image, had already said that it will not use those weapons under any circumstances.\n\nShaara said in a written statement shared exclusively with Reuters by his office that the group is now working to \"dissolve the security forces of the previous regime and close the notorious prison,\" where the government of toppled dictator Bashar al-Assad is estimated to have held tens of thousands of detainees.\n\nHe reiterated that he will form a government of technocrats. The current transitional government is set to rule until March 2025, according to a statement by his group.\n\nThe Pentagon, in response, said the US welcomes his comments about securing potential chemical weapons sites, but cautioned that \"actions have to meet words as well.\"\n\nGolani's comments came as Israel has carried out massive strikes targeting the Assad regime's military assets, including chemical weapons sites, amid fears that former Syrian army weaponry could fall into the hands of hostile forces in the country, as well as the Iran-backed Hezbollah in Lebanon.\n\nA monitor of the Syrian civil war reported fresh Israeli airstrikes on Wednesday that targeted Assad-linked sites in the coastal provinces of Latakia and Tartus.\n\n\"Israeli warplanes launched air strikes\" targeting \"military sites\" including \"the Latakia port\" as well as warehouses in neighboring Tartus province, the Syrian Observatory for Human Rights said, adding that \"Israeli warplanes continue to destroy what remains of Syria's military arsenal for the fourth consecutive day since the fall of the former regime.\"\n\nMeanwhile, US Defense Secretary Lloyd Austin told Israeli counterpart Israel Katz during a phone call Wednesday that it was important for the United States and Israel to be in close consultation over events unfolding in Syria, the Pentagon said.\n\nAustin told Katz that Washington was monitoring developments in Syria and that it backed a peaceful, inclusive political transition, according to the Pentagon. He added that the US would continue its mission to prevent the Islamic State extremist group from reestablishing a safe haven in Syria.\n\n\"Secretary Austin emphasized the importance of close consultation between the United States and Israel on events in Syria,\" the Pentagon said.\n\nThe Pentagon also said that Austin discussed with Katz attempts to secure Israeli hostages in Gaza and urged Israel to improve the humanitarian situation in the Palestinian enclave where Israel's military is fighting against Hamas, whose terror attack on October 7, 2023, sparked the ongoing war.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [],
            "image": "https://static-cdn.toi-media.com/www/uploads/2024/12/AP24344694173682-e1733976259588.jpg",
            "eventUri": "eng-10165976",
            "sentiment": 0.2156862745098038,
            "wgt": 69,
            "relevance": 1
        },
        {
            "uri": "8442833724",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-05",
            "time": "00:05:23",
            "dateTime": "2024-12-05T00:05:23Z",
            "dateTimePub": "2024-12-05T00:05:07Z",
            "dataType": "news",
            "sim": 0.6039215922355652,
            "url": "https://forward.com/news/679942/amnesty-international-israel-genocide-gaza/",
            "title": "Amnesty International says Israel is committing genocide in Gaza",
            "body": "Amnesty International said Wednesday that Israel is committing genocide in Gaza, lending the credibility of one of the world's best-known human rights organizations to a claim that activists and some legal scholars have been making for more than a year.\n\nAmnesty is the largest human rights group to definitively describe as genocide Israel's prosecution of the war in Gaza that was spawned by the Oct. 7 Hamas terror attack.\n\nThe organization said that Israel has sought to at least partly destroy the Palestinian people through indiscriminate attacks on civilians in Gaza, repeated evacuation orders, limits on humanitarian aid and other measures that cannot be justified as essential to its legitimate military operation against Hamas. That led to the conclusion, backed by a nearly 300-page report and more than 200 interviews, that the Genocide Convention's requirement of \"intent\" applies.\n\n\"We could find only one reasonable inference and conclusion,\" said Agnès Callamard, secretary general of Amnesty, \"which is that, either in addition to -- or in order to -- deliver military objectives Israel intended to commit genocide.\"\n\nPrevious reports from both Amnesty and Human Rights Watch accusing Israel of apartheid helped cement that view among international rights groups. Human Rights Watch has not made a determination as to whether Israel is committing genocide in Gaza.\n\nThe accusation that Israel is committing genocide against the Palestinians predates the current war, but became far more pronounced and widespread after Israel began its furious response to the attack last October in which Palestinian terrorists killed some 1,200 people in Israel and kidnapped another 250. Israel dropped more than 29,000 bombs on the 141-square-mile territory in two months; international officials say more than 44,000 Palestinians in the strip have been killed to date, and nearly all of Gaza's 2 million residents displaced and at risk of starvation.\n\nDozens of legal scholars and academics initially warned of a \"potential genocide\" in Gaza. The Lemkin Institute for Genocide Prevention described it as a genocide in December 2023, and Genocide Watch, a monitoring group, said in Febraury that Israel's activity had \"included many acts of genocide.\" The International Court of Justice ruled that it was \"plausible\" Israel's actions amounted to genocide that same month, and in May a consortium of international law experts from Yale, Cornell and Boston University said that Israel was committing genocide.\n\nThose allegations have been met with derision by Israel and its defenders, who generally say that Palestinian civilian casualties have been exaggerated and that Hamas is to blame for them because it embeds its fighters in dense urban areas and steals aid.\n\nArsen Ostrovsky, chief of the International Legal Forum, a pro-Israel group, called the Amnesty report \"nothing short of a blood libel against the Jewish state.\"\n\nOren Marmorstein, an Israeli government spokesperson, denounced the report a week before it was even released, telling the New York Post: \"The deplorable and fanatical organization Amnesty International has produced a fabricated report entirely based on lies.\"\n\nIn its report, Amnesty says that it reviewed statements by Israeli government and military officials, and their submissions to the Israel Supreme Court, but had \"received no substantive answers\" to letters sent to Israeli authorities between Oct. 30, 2023, and Oct. 16, 2024, requesting meetings and information.\n\nMuch of Amnesty's report consists of detailing damage to civilian infrastructure in Gaza, including the destruction of mosques and universities that did not appear to have any connection to Hamas. By July, the group says, 63% of all structures in Gaza had been damaged or destroyed, including 85% of all schools.\n\n\"It's known they are fighting Hamas and one might suppose that they'd bomb any place in which it would seek refuge, but when they bomb the Gaza public library, the unknown soldier monument, the Rashad al-Shawa Cultural Centre -- where Bill Clinton met with the legislative council -- they're bombing the city's landmarks,\" a municipal worker in Gaza City told Amnesty researchers. \"Their intent is for the city to have a different face after the war.\"\n\nBut international law does not define the crime of genocide solely based on the extent of destruction or even death in a designated group. It requires that the violence against that group be done with \"specific intent\" to destroy it, at least in part, which is often difficult or impossible to prove. Amnesty pointed to what it described as statements from senior Israeli officials encouraging the destruction of Palestinian society in Gaza and erasing distinctions between combatants and civilians.\n\nFor example, a few days after Oct. 7, Gen. Ghassan Alian, who manages the unit in charge of Palestinian civilian life in the occupied West Bank and Gaza, recorded a video in Arabic promising to punish the local population.\n\n\"The citizens of Gaza are celebrating, instead of being horrified,\" Alien said in the video. \"With such human beasts, we will deal accordingly. Israel has imposed a complete blockade on Gaza. You will not have electricity or water, just destruction. You want hell, you'll get hell.\"\n\nThe report also highlighted several references by Prime Minister Benjamin Netanyahu to \"Amalek,\" the Israelites' biblical enemy, which God commanded the Jewish people to exterminate completely.\n\nCallamard, the French human rights attorney who has run Amnesty since 2021, said at a Wednesday briefing for reporters that Israeli soldiers in Gaza appeared to have acted on these statements. \"I am coming to conquer Gaza ... to blot out the memory of Amalek,\" soldiers sing in one video referenced in the report. \"We know our slogan: 'There are no uninvolved civilians.'\"\n\nIsraeli military and political officials say their soldiers take extensive measures to protect Palestinian civilians, including delivering warnings in advance of strikes and issuing evacuation orders, But Amnesty said in its report that these measures were insufficient and sometimes have themselves represented violations of international laws regarding warfare.\n\nThe report said, for example, that Israel had issued 59 different evacuation orders since the war began that were \"sweeping, often incomprehensible to the local population, misleading and arbitrary.\"\n\nOstrovsky, the legal scholar, and organizations including Genocide Watch have also accused Hamas of committing acts of genocide in its Oct. 7 attack against Israel. At Wednesday's briefing, Amnesty officials did not respond to a question about whether they had evaluated that question.\n\nBut Amnesty did say that it is in the process of completing a second, comprehensive report on the violence committed by Hamas and other Palestinian militants on Oct. 7, and that some of their actions -- including \"deliberate mass killings\" in Israel -- constituted war crimes.\n\nThe organization also acknowledged that \"Hamas and other Palestinian armed groups endangered Palestinian civilians through their conduct by operating from, or in the vicinity of, densely populated residential areas.\" But Amnesty noted that fact \"does not release Israel from its own obligations under international humanitarian law.\"\n\nThe report calls on Israel and Hamas to reach an immediate ceasefire, and for Hamas to release all Israeli hostages it is currently holding and allow the Red Cross to visit those in captivity. Some 100 hostages remain in captivity, though at least a third are believed dead.\n\nAmnesty tends to take a more emotional approach to its advocacy than some other human rights groups, and that was on display during Wednesday's briefing unveiling the genocide report. Cammard repeatedly criticized international governments for failing to take enough action to stop the war and described the organization's research as having been conducted with \"blood, with commitment, with anger.\"\n\nBudour Hassan, an Amnesty researcher in Israel and the West Bank, described the influence of Gaza residents who shared their stories with her team: \"They wanted to tell the world that what is happening has only one name and we should not be shy of saying that name: It is genocide.\"",
            "source": {
                "uri": "forward.com",
                "dataType": "news",
                "title": "The Forward"
            },
            "authors": [
                {
                    "uri": "arno_rosenfeld@forward.com",
                    "name": "Arno Rosenfeld",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://forward.com/wp-content/uploads/2024/12/GettyImages-1225711060-scaled.jpg",
            "eventUri": "eng-10135399",
            "sentiment": -0.2549019607843137,
            "wgt": 67,
            "relevance": 1
        },
        {
            "uri": "8434735240",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-29",
            "time": "12:34:41",
            "dateTime": "2024-11-29T12:34:41Z",
            "dateTimePub": "2024-11-29T12:34:19Z",
            "dataType": "news",
            "sim": 0.729411780834198,
            "url": "https://www.westernjournal.com/islamist-nightmare-school-girl-confesses-trick-ended-innocent-teachers-beheading/",
            "title": "Islamist Nightmare: School Girl Confesses Trick That Ended in Innocent Teacher's Beheading",
            "body": "A new detail has emerged in the 2020 murder of a 47-year-old schoolteacher in France.\n\nSamuel Paty was murdered by an 18-year-old Chechen refugee, Abdoullakh Anzorov, on Oct. 16, 2020, the U.K.'s Daily Mail reported. Anzorov stabbed Paty to death outside of the school he worked at then decapitated him.\n\nAnzorov targeted Paty after an online harassment campaign drew attention to the teacher for his apparent \"Islamophobia\" in the classroom.\n\nHowever, in a court hearing on Tuesday, the student who made the original accusation admitted to lying about the whole thing before apologizing to his family.\n\nThe girl, who was 13 at the time of the murder, claimed Paty showed caricatures of Muhammad in class from the magazine Charlie Hebdo and told all his Muslim students to leave the classroom.\n\nShe admitted that she made the story up and that she had not been in class that day. She had been suspended for bad behavior for two days and decided to lie to avoid punishment from her parents.\n\nPaty did show cartoons of Muhammad from Charlie Hebdo as part of a class to discuss the terror attack from 2015, but he never told Muslim students to leave the room.\n\nThe Mail reported, Paty instructed students to turn away if they chose after explaining that the images were being shown as part of a lesson on ethics.\n\nThe Jan. 7, 2015, attack on Charlie Hebdo's office, which left 12 dead, was carried out by several Muslim men, who sought revenge for the magazine's depictions of Islam and Muhammad. Al-Qaeda later claimed responsibility.\n\nThe girl's father, Brahim Chnina, has been accused of being involved in the online campaign against Paty. He faces charges of association with a terrorist organization.\n\nThe schoolgirl received a suspended sentence of 18 months for her role in Paty's murder. Five of her classmates also faced charges, with four of them being handed suspended sentences and one being given a \"six-month term with an electronic tag.\"\n\nPaty's death was based on a lie following an ethics lesson.\n\nHe did not mock or slander Muhammad or Islam, but what if he had?\n\nDoes an innocent man deserve to be brutally murdered and beheaded for those actions? No.\n\nAdvertise with The Western Journal and reach millions of highly engaged readers, while supporting our work. Advertise Today.",
            "source": {
                "uri": "westernjournal.com",
                "dataType": "news",
                "title": "The Western Journal"
            },
            "authors": [
                {
                    "uri": "samuel_short@westernjournal.com",
                    "name": "Samuel Short",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://www.westernjournal.com/wp-content/uploads/2024/11/Samuel-Paty.jpg",
            "eventUri": "eng-10121429",
            "sentiment": -0.5215686274509803,
            "wgt": 67,
            "relevance": 1
        },
        {
            "uri": "2024-12-573376882",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-12",
            "time": "02:56:39",
            "dateTime": "2024-12-12T02:56:39Z",
            "dateTimePub": "2024-12-12T02:55:34Z",
            "dataType": "news",
            "sim": 0.572549045085907,
            "url": "https://www.timesofisrael.com/young-boy-killed-several-bus-passengers-wounded-in-west-bank-terror-shooting/",
            "title": "Young boy killed, several bus passengers wounded in West Bank terror shooting",
            "body": "A young boy was fatally shot and several people wounded in a terror attack targeting a Jerusalem-bound bus in the West Bank late Wednesday night.\n\nThe child was brought in critical condition to Hadassah Hospital Ein Kerem in nearby Jerusalem, where doctors declared his death early Thursday following intensive efforts to save him.\n\nThe boy was not immediately named. The Magen David Adom ambulance service identified him as a 12-year-old while the municipality of the Beitar Illit settlement -- where the bus departed from -- said in a statement that he was traveling home to Jerusalem with his family.\n\nThree others were wounded in the shooting -- a woman with moderate wounds and two people who were lightly hurt.\n\nThe bus was shot up by the gunman at a junction by the Palestinian town of al-Khader, the Israel Defense Forces said, before proceeding with the wounded to the Tunnels Checkpoint.\n\nThe terrorist remains at large. The IDF announced troops were setting up roadblocks while encircling Bethlehem as part of the manhunt.\n\nA video clip filmed shortly after the shooting showed passengers fleeing the bus after it arrived at the checkpoint, as security forces there rushed toward the vehicle amid the sound of gunfire. It was not clear from the footage where all the shots emanated from.\n\nThe attack came after three Israelis were lightly injured by gunfire the previous night while visiting Joseph's Tomb in the Palestinian city of Nablus without coordinating with the military, and also followed a car-ramming attack in the southern West Bank over the weekend in which a soldier was seriously wounded.\n\nViolence has risen sharply in the West Bank since the Gaza war started on October 7, 2023, when thousands of Hamas-led terrorists stormed southern Israel to kill some 1,200 people and take 251 hostages.\n\nSince then, 42 people, including Israeli security personnel, have been killed in terror attacks in Israel and the West Bank. Another six members of the security forces were killed in clashes with operatives in the West Bank amid a major counterterrorism offensive that has been accompanied by sharp restrictions on Palestinian movement.\n\nIsraeli troops have arrested some 5,250 wanted Palestinians across the West Bank as part of the post-October 7 military operations, including more than 2,050 affiliated with Hamas.\n\nAccording to the Palestinian Authority health ministry, some 800 West Bank Palestinians have been killed in the same span of time. The IDF says the vast majority of them were gunmen killed in exchanges of fire, rioters who clashed with troops or terrorists carrying out attacks.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [
                {
                    "uri": "israeli_security_forces@timesofisrael.com",
                    "name": "Israeli Security Forces",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://static-cdn.toi-media.com/www/uploads/2024/12/AP24346819858040-e1733966787448.jpg",
            "eventUri": "eng-10165678",
            "sentiment": -0.3647058823529412,
            "wgt": 66,
            "relevance": 1
        },
        {
            "uri": "8448483379",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-09",
            "time": "00:06:09",
            "dateTime": "2024-12-09T00:06:09Z",
            "dateTimePub": "2024-12-09T00:06:01Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.theblaze.com/abide/biblical-prophecy-and-israel-are-predictions-unfolding-before-our-eyes",
            "title": "Biblical prophecy and Israel: Are predictions unfolding before our eyes? | Blaze Media",
            "body": "'I don't believe Israel's under judgment. ... In other words, God didn't send this enemy, but God ... allowed it.'\n\nAuthor Joel Rosenberg believes some of the events unfolding around us hold biblical significance, particularly when it comes to Israel and the Middle East.\n\nRosenberg, an expert on biblical prophecy who now lives in Israel, recently spoke with CBN News about Hamas, the war in Gaza, and how current events might play into what the Bible says about future happenings and the end of days.\n\n\"That is the No. 1 question I'm getting asked. ... 'Can you put this [current moment] in a prophetic context?'\" Rosenberg said. \"I would say, No. 1, we're definitely in a birth pang, right? Jesus speaks in Matthew 24 that there's going to be contractions and releases, moments of wars and rumors of wars, and kingdom against kingdom, nation against nation, as well as earthquakes and famines and other disasters.\"\n\nHe continued, \"Those are contractions, and just like when your wife gets close to delivering ... the contractions are longer and more painful, and the release moments are shorter.\"\n\nRosenberg said Israelis were living in a time of release on Oct. 6, 2023, as it was safe, prosperous, and secure -- the safest it had been in modern history.\n\n\"You'd have to go back to the days of Solomon and David when the kingdom was peaceful and secure,\" he said, noting that Israel had just come off making four Arab-Israeli peace treaties and normalization treaties via the Abraham Accords. \"We were just about to finalize another deal -- the biggest peace and normalization deal in Israeli history -- and that would be with the Saudi government.\"\n\nBut all of that peace was obliterated by Hamas' horrific terror attack on Oct. 7, 2023, an event he said was the \"longest contraction\" modern Israel has faced.\n\n\"I would add that, just in context, I believe COVID was a biblical Matthew 24 contraction where ... a lot of people died. But the other part was ... not only was there this terrible health pandemic, plague, a biblical plague, but even the American government could say in an instant, 'You can't go to church. You can't leave your house. You can't go see your friends, but the strip clubs could stay open. The casinos could stay open. The bars could stay open, the liquor stores, but not churches. That was a contraction.\"\n\n'There's no question in my mind that we're seeing the chess pieces on the board align in a manner that's consistent with the prerequisites of Ezekiel 38-39.'\n\nAnother contraction, he said, is Russia's prolonged war in Ukraine, a chaotic and deadly ongoing event further creating international stability.\n\nRosenberg cited Amos 9:9 while discussing Israel's current war after the Hamas invasion. That verse reads (NIV): \"For I will give the command, and I will shake the people of Israel among all the nations as grain is shaken in a sieve, and not a pebble will reach the ground.\"\n\nHe believes Amos 9:9 is a recurring prophecy but that the current war in Israel is another \"shaking\" that falls under its umbrella.\n\n\"I don't believe Israel's under judgment. ... In other words, God didn't send this enemy, but God ... allowed it,\" Rosenberg said. \"Why? To shake us, to help us realize that most Israelis either haven't read, don't remember, or don't care about Psalm 23, in which David, our greatest king, told us the Lord is our shepherd.\"\n\nHe said some Israelis forgot, due to security, the realities inherent in this scripture.\n\n\"We forgot as a nation that there are ravenous wolves trying to destroy us,\" he said. \"It shows what a moment of release of security we felt like we were in. But I think this is a wake-up call.\"\n\nAs for the Palestinians of Gaza, Rosenberg said he believes they are facing a \"biblical judgment,\" appealing to Genesis 12:1-3 (NIV) to make his case. Those verses read:\n\nThe Lord had said to Abram, \"Go from your country, your people and your father's household to the land I will show you. \"I will make you into a great nation, and I will bless you; I will make your name great, and you will be a blessing. I will bless those who bless you, and whoever curses you I will curse; and all peoples on earth will be blessed through you.\"\n\nRosenberg said the Abrahamic Covenant makes it clear that God will bless those who bless Israel and curse those who do not.\n\n\"If you curse Israel every day for 76 years, and you want to ... elect a genocidal government, even if later you don't want that, but what are you going to do now?\" he said. \"I believe we're seeing a judgment. Doesn't mean God doesn't want to show mercy. Also, we need to pray as Christians. Who else is praying for the Palestinians? We need to be. We need to show compassion. But there's a judgment going on from 76 years of hatred, hostility, cursing, and now, you know, an attempt at genocide against Israel and the Jewish people.\"\n\nConsidering the prophetic verses in Bible books like Ezekiel -- particularly the Gog and Magog prophecy -- Rosenberg broke down his beliefs on what's happening now and how it might relate.\n\n\"In terms of watching where we are going, there's no question in my mind that we're seeing the chess pieces on the board align in a manner that's consistent with the prerequisites of Ezekiel 38-39 happening, the war of Gog and Magog,\" Rosenberg said, referring to the Bible chapters that purportedly predict Russia, Iran, and Turkey attempting to invade Israel.\n\nBut Rosenberg was also careful in addressing these issues, reminding Christians not to read too closely into what's happening. He said dynamics can and do quickly shift.\n\n\"I just want to caution people who are interested in those prophecies ... don't try to jump to a fast conclusion,\" he said. \"The data doesn't support yet a conclusion, but it definitely supports [the premise], 'Isn't this interesting?'\"",
            "source": {
                "uri": "theblaze.com",
                "dataType": "news",
                "title": "TheBlaze"
            },
            "authors": [],
            "image": "https://www.theblaze.com/media-library/biblical-prophecy-and-israel-are-predictions-unfolding-before-our-eyes.jpg?id=55157652&width=1200&height=600&coordinates=0%2C27%2C0%2C28",
            "eventUri": None,
            "sentiment": -0.05098039215686279,
            "wgt": 66,
            "relevance": 1
        },
        {
            "uri": "2024-11-561021902",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-29",
            "time": "15:08:23",
            "dateTime": "2024-11-29T15:08:23Z",
            "dateTimePub": "2024-11-29T15:07:02Z",
            "dataType": "news",
            "sim": 0.6784313917160034,
            "url": "https://www.timesofisrael.com/senior-uae-official-flies-to-israel-for-condolence-visit-to-family-of-murdered-rabbi/",
            "title": "Senior UAE official flies to Israel for condolence visit to family of murdered rabbi",
            "body": "Zvi Kogan, a Chabad rabbi who was murdered in the UAE in November 2024. (Courtesy: Chabad)\n\nA senior Emirati official flew to Israel on Friday especially to pay a condolence visit to the family of Chabad Rabbi Zvi Kogan, who was killed in an apparent terror attack in the United Arab Emirates, Hebrew-language media reported.\n\nDr. Ali Rashid Al Nuaim, a member of the UAE's Federal Supreme Council, attended the shiva in Kfar Chabad, where he told relatives of the murdered man that the UAE is committed to \"openness and peace,\" and vowed that Kogan's legacy will endure.\n\n\"We will never allow extremists to separate us,\" he said.\n\nKogan, a 28-year-old UAE-based rabbi, went missing last Thursday and was found dead by security services on Sunday.\n\nIsraeli officials have said Kogan was targeted because he was Jewish and branded his killing as an antisemitic terror attack. Israeli agencies are assisting in the investigation.\n\nSenior Israeli officials, including Prime Minister Benjamin Netanyahu and President Isaac Herzog, have thanked Emirati authorities for their swift action on the case, and vowed that the killing will not damage ties between the nations.\n\nThe circumstances of Kogan's death have not been disclosed and it is unclear if Emirati authorities have established a motive.\n\nEarlier this week, the UAE published the names and photographs of three suspects it is holding in the murder. All three men are Uzbek nationals, according to the UAE Interior Ministry -- Olimpi Toirovich, 28; Makhmudjon Abdurakhim, 28; and Azizbek Kamlovich, 33.\n\nThe ministry described the three as \"the perpetrators of the murder of the Moldovan citizen.\" Kogan held dual Israeli-Moldovan citizenship.\n\nAccording to Kan, Israeli officials believe that Kogan's killing was not necessarily carried out on behalf of Iran, but that it was a terror attack.\n\nKogan worked in the UAE for Chabad, which seeks to support Jewish life for thousands of Jewish visitors and residents in the Gulf Arab state.\n\nHe had been living in the UAE for several years. Last Thursday, he vanished in Dubai, where he ran a kosher grocery store, and his body was found on Sunday in the Emirati city of Al Ain, which borders Oman, around 150 kilometers (93 miles) from Abu Dhabi.\n\nHe was buried at Jerusalem's Mount of Olives cemetery.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [
                {
                    "uri": "zvi_kogan@timesofisrael.com",
                    "name": "Zvi Kogan",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://static.timesofisrael.com/www/uploads/2024/11/zvi-2copy.jpg",
            "eventUri": "eng-10119195",
            "sentiment": -0.388235294117647,
            "wgt": 65,
            "relevance": 34
        },
        {
            "uri": "8424137656",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-22",
            "time": "14:53:51",
            "dateTime": "2024-11-22T14:53:51Z",
            "dateTimePub": "2024-11-22T14:53:31Z",
            "dataType": "news",
            "sim": 0.7176470756530762,
            "url": "https://www.nbcnews.com/news/world/arrest-netanyahu-icc-warrant-divides-world-israel-gaza-rcna181320",
            "title": "Who would arrest Netanyahu? ICC warrant for Israeli leader draws a global dividing line",
            "body": "Hungary pledged Friday to defy the International Criminal Court, breaking with many of its European neighbors.\n\nThe arrest warrant against Israeli Prime Minister Benjamin Netanyahu forced a reckoning Friday for the U.S. ally's global status more than a year after it launched its devastating war in Gaza.\n\nThe warrants -- also issued for former Israeli Defense Minister Yoav Gallant and Hamas military chief Mohammed Deif -- drew a diplomatic dividing line between countries who vowed to back the International Criminal Court and those who pledged to defy it.\n\nWhile he faces accusations of war crimes and crimes against humanity for leading his country's assault on the Palestinian enclave, Netanyahu is unlikely to be in handcuffs any time soon -- as long as he avoids trips to Ireland, Italy and the Netherlands, who all made clear they would arrest him if he visits.\n\nHungary, in contrast, promised not to arrest the Israeli leader. Its strongman leader Viktor Orbán sent a letter condemning the decision and inviting Netanyahu for an official visit on which he promised to \"ensure your safety and freedom.\"\n\nThe Israeli leader praised Hungary, who he said had \"like our friends in the U.S.,\" shown \"moral clarity and steadfastness on the side of justice and the truth.\" He contrasted this to what he called the \"shameful weakness of those who have lined up alongside the outrageous decision.\"\n\nThe White House said Thursday that President Joe Biden's administration was \"deeply concerned by the prosecutor's rush to seek arrest warrants and the troubling process errors that led to this decision.\"\n\nNeither Israel nor the U.S. recognizes the jurisdiction of the ICC, which is based in The Hague, the Netherlands, and has no police to enforce its warrants.\n\nUnder the Rome statute that created the ICC, its signatories are obliged to carry out arrest warrants, no matter the rank of the accused. But most governments also abide by the international legal principle that heads of state have legal immunity from other courts.\n\nThe court said in its statement that there was reason to believe that Netanyahu and Gallant used \"starvation as a method of warfare\" by restricting humanitarian aid and intentionally targeting civilians in Israel's campaign in Gaza -- charges Israeli officials dismissed as False and antisemitic.\n\nThe arrest warrants were announced on the same day that the death toll in the enclave passed 44,000, according to local officials, and followed mounting international condemnation over the dire humanitarian situation in the Palestinian enclave. The World Health Organization has warned that northern Gaza is at imminent risk of famine, while health organizations have deemed it necessary to vaccinate hundreds of thousands of children for polio in recent months.\n\nIsrael launched its campaign following the Oct. 7 terror attack in which Israeli officials said some 1,200 people were killed and around 250 taken hostage, a major escalation in the decadeslong conflict.\n\nMohammed Deif was accused of crimes against humanity and war crimes, including for his role as a mastermind of Oct. 7.\n\nSome European countries have not said whether they would arrest Netanyahu if he visited, including a number of Israeli allies.\n\nBritain respects the independence of the ICC, Prime Minister Keir Starmer's spokesperson said, but did not say whether Britain would arrest Netanyahu.\n\nFrance restated its commitment to the court's independence and said its response would align with the statutes of the court, but a spokesperson for its foreign ministry did not explicitly say how Paris would act.\n\nThe German government noted its role in drafting the ICC statutes but also its relationship with Israel, vowing to \"carefully examine\" the next steps.\n\nOthers, including Sweden and Norway, were also noncommittal.\n\nSome appeared split, with both Austrian and Czech governments promising to uphold their obligations to the ICC while senior officials criticized the arrest warrants.\n\nCzech Prime Minister Petr Fiala called the ICC decision \"unfortunate,\" saying on X late on Thursday that it \"undermines its authority in other cases when it equates the elected representatives of a democratic state with the leaders of an Islamist terrorist organization.\" Austrian Foreign Minister Alexander Schallenberg said the warrants being issues was absurd.\n\nCountries across the Middle East also praised and backed the court, as did South Africa, which has accused Israel of genocide in Gaza at the International Court of Justice. Israel and the U.S. deny those charges.\n\nPope Francis suggested the global community should study whether Israel's military campaign in Gaza constitutes a genocide of the Palestinian people, in comments published Sunday that were some of his most explicit criticism yet of Israel's conduct.\n\nThe trio facing the arrest warrants join a group that includes Russian President Vladimir Putin, who has been subject to an ICC arrest warrant over alleged war crimes in Ukraine since last year.",
            "source": {
                "uri": "nbcnews.com",
                "dataType": "news",
                "title": "NBC News"
            },
            "authors": [],
            "image": "https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1024-512,f_auto,q_auto:best/rockcms/2024-11/241122-israel-benjamin-netanyahu-mn-0855-d4591d.jpg",
            "eventUri": "eng-10105884",
            "sentiment": -0.0980392156862745,
            "wgt": 63,
            "relevance": 1
        },
        {
            "uri": "8450900566",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-10",
            "time": "11:35:44",
            "dateTime": "2024-12-10T11:35:44Z",
            "dateTimePub": "2024-12-10T11:35:28Z",
            "dataType": "news",
            "sim": 0.7764706015586853,
            "url": "https://www.cbsnews.com/news/netanyahu-corruption-trial-israel-pm-on-stand-amid-gaza-war-syria-chaos/",
            "title": "Israel's Netanyahu takes stand in corruption trial as war in Gaza grinds, neighboring Syria's dictator falls",
            "body": "Tel Aviv, Israel -- Israeli Prime Minister Benjamin Netanyahu took the stand Tuesday in his long-running trial for alleged corruption, setting off what's expected to be a weekslong spectacle that will draw unwelcome attention to his legal woes as he faces an international arrest warrant for war crimes and the fighting in Gaza continues. It is the first time a sitting Israeli prime minister takes the stand as a criminal defendant, an embarrassing milestone for a leader who has tried to cultivate an image as a sophisticated and respected statesman.\n\nUpon starting his testimony, Netanyahu said \"hello\" to the judges. One judge told him he had the same privileges as other witnesses and could sit or stand as he chose.\n\n\"I waited eight years for this moment, to say the truth,\" Netanyahu said, standing at a podium in a packed Tel Aviv courtroom. He called the charges against him \"an ocean of absurdness\" and promised his version would cut through the prosecution's case.\n\nNetanyahu appeared at ease as he began telling his version of events and shared personal details about his life that he might hope would shape the judges' perception of him. He said he used to lose sleep over media coverage but learned it had no meaningful bearing -- in contrast to the prosecution's attempts to paint him as image-obsessed.\n\nHe said he smoked cigars but could hardly finish them because of his workload, but hated champagne. One case revolves around him receiving a \"supply line\" of cigars and champagne from billionaire associates.\n\nHis lawyer asked that he be allowed to receive notes while testifying to help ensure he can continue running the country.\n\nNetanyahu will answer during his court appearances to charges of fraud, breach of trust and accepting bribes in three separate cases.\n\nHe is accused of accepting tens of thousands of dollars' worth of cigars and champagne from a billionaire Hollywood producer in exchange for assisting him with personal and business interests. He is also accused of promoting advantageous regulation for media moguls in exchange for favorable coverage of himself and his family.\n\nNetanyahu, 75, denies wrongdoing, saying the charges are a witch hunt orchestrated by a hostile media and a biased legal system out to topple his lengthy rule. His testimony caps years of scandals that have swirled around him and his family.\n\nThe testimony, set to take place six hours a day, three days a week for several weeks, will take up a significant chunk of Netanyahu's working hours, prompting critics to ask if he can capably manage a country embroiled in a war on one front, containing the fallout from a second, and keeping tabs on other potential regional threats, including from Iran or the recent fall of longtime dictator Bashar al-Assad in neighboring Syria.\n\nNetanyahu, in his testimony, said he could \"find a balance\" between both commitments.\n\nDozens of people gathered outside of the court in Tel Aviv, some protesting against Netanyahu, including family members of hostages held in Gaza, and also a group of his supporters. A banner draped in front of the court read: \"Crime Minister.\"\n\nUnder Israeli law, indicted prime ministers are not required to step down. But the charges against Netanyahu cleaved deep divisions in Israel, with protesters demanding he resign and former political allies refusing to serve in government with the Israeli leader, triggering a political crisis that led to five elections in less than four years beginning in 2019. He overcame the political tumult only two years ago by striking an agreement with smaller right-wing parties that had long languished on the edges of Israeli politics, to form the country's most far-right government ever.\n\nNetanyahu's supporters view the charges as the result of the justice system's bias and overreach, while his opponents have accused him of prolonging the raging war in Gaza in a bid to distract from, if not delay his own court proceedings. Netanyahu launched the war on Gaza's Hamas rulers immediately after they carried out their brutal Oct. 7, 2023 terror attack on Israel, killing some 1,200 people and taking 251 others hostage.\n\nDespite the pressure, the polarizing Netanyahu has rejected calls to step down and has used his position as prime minister to lash out at law enforcement, media and courts.\n\nAn Israeli court rejected a request by Netanyahu's lawyers to reduce the expected testimony hours, as well as several other requests to delay its start, which they said were necessary because of the prime minister's busy schedule and the country's significant challenges. A verdict isn't expected until 2026 at the earliest and Netanyahu will have the option to appeal at the Supreme Court.\n\nThe court has spent months hearing prosecution witnesses in the three cases, including some of Netanyahu's once closest aides who turned state witnesses. The prosecution has tried to portray the prime minister as an image-obsessed leader who broke the law to improve his public perception.\n\nThe most damaging case against Netanyahu involves an influence-peddling scandal in which two of his formerly closest aides have testified against him on suspicions of promoting regulation worth hundreds of millions of dollars to Israel's Bezeq telecom company. In return, Bezeq's popular news site, Walla, allegedly provided favorable coverage of Netanyahu and his family.\n\nNetanyahu is also alleged to have offered a newspaper publisher legislation that would weaken his paper's main rival in return for more favorable coverage.\n\nMoreover, the prime minister is accused of accepting nearly $200,000 in champagne and cigars from Hollywood producer Arnon Milchan and in exchange, he allegedly operated on Milchan's behalf on U.S. visa matters, tried to legislate a generous tax break for him and sought to promote his interests in the Israeli media market.\n\nNetanyahu's testimony could further tarnish his image at a complicated time for Israel's longest-serving leader. His popular support dropped after the Hamas attack in October 2023, with the public blaming his leadership for failing to prevent the assault, and if elections were held today polls suggest he would struggle to form another new government.\n\nIsrael is still fighting Hamas in Gaza with no end in sight, despite heavy international pressure to wind down the war, as well as pressure from the families of hostages still held in Gaza and their supporters to bring their loved ones home.\n\nThe Israeli leader, along with his former defense minister, also faces an arrest warrant from the International Criminal Court for war crimes charges related to the war in Gaza, which his office has dismissed as \"absurd and False actions and charges.\"",
            "source": {
                "uri": "cbsnews.com",
                "dataType": "news",
                "title": "CBS News"
            },
            "authors": [],
            "image": "https://assets1.cbsnewsstatic.com/hub/i/r/2024/12/10/c906ffa3-4266-4f95-b816-c04e9870a015/thumbnail/1200x630/55a8283e1d8e4def62768c8743f75ab9/netanyahu-corruption-trial-2188597367.jpg?v=d633d0331cc96a4353754b3de830df72",
            "eventUri": "eng-10154064",
            "sentiment": -0.02745098039215688,
            "wgt": 62,
            "relevance": 1
        },
        {
            "uri": "8463767348",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-18",
            "time": "18:03:46",
            "dateTime": "2024-12-18T18:03:46Z",
            "dateTimePub": "2024-12-18T18:02:45Z",
            "dataType": "news",
            "sim": 0.4666666686534882,
            "url": "https://www.breitbart.com/middle-east/2024/12/18/oil-rich-iran-short-of-fuel-electricity-billions-spent-on-terror/",
            "title": "Oil-rich Iran Short of Fuel, Electricity; Billions Spent on Terror",
            "body": "Iran is in the midst of a fuel shortage and an electricity crisis, causing essential utilities to be shut down in the middle of a cold winter. The regime has failed to provide for its own people but has spent billions of dollars on terror abroad.\n\nAl Jazeera reported Wednesday:\n\nTens of millions of people across Iran are facing major disruptions as authorities shut down services in the face of an exacerbating energy and currency crisis amid historic regional tensions.\n\nThis week, government offices, schools, banks and businesses in major provinces and in the capital Tehran have been largely closed due to worsening fuel and power shortages as temperatures dropped to subzero levels.\n\nEnergy Minister Abbas Aliabadi said on Wednesday that 13 power plants are out of commission due to a lack of fuel.\n\nIran was the fourth-largest oil producer in OPEC last year, according to the U.S. Energy Information Administration. Yet it cannot provide for its own fuel needs -- despite the easing of sanctions by the Biden-Harris administration.\n\nAlready plagued by chronic air pollution and water shortages, the Iranian regime also faces a collapsing currency and decaying infrastructure, as its terrorist proxies continue to lose the war against Israel they started with the Hamas terror attack last October 7, and as Israel plans a possible attack to destroy Iran's nuclear weapons program.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/12/Iran-power-shortage-Associated-Press-e1734539403466.jpg",
            "eventUri": "eng-10177358",
            "sentiment": -0.4745098039215686,
            "wgt": 62,
            "relevance": 1
        },
        {
            "uri": "8430360128",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "20:44:49",
            "dateTime": "2024-11-26T20:44:49Z",
            "dateTimePub": "2024-11-26T20:44:30Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://redstate.com/terichristoph/2024/11/26/antisemitic-brands-youll-want-to-avoid-this-black-friday-n2182487",
            "title": "The Antisemitic Brands You'll Want to Steer Clear of This Holiday Shopping Season",
            "body": "The opinions expressed by contributors are their own and do not necessarily represent the views of RedState.com.\n\nIt's that time of year again, when holiday shopping kicks into overdrive and companies start offering steep discounts in order to move merchandise from their stores to your house.\n\nIn previous years, RedState has highlighted companies who didn't deserve your hard-earned cash due to their embrace of DEI and woke ideologies. We're happy to report that, this year, good progress is being made in shaming companies into revoking the kind of leftist policies that send conservatives running in the opposite direction.\n\nOur own Bob Hoge wrote of the excellent work Robby Starbuck has done to help corporations like Walmart come to the conclusion that it's bad for business to pander to the weirdos.\n\nActivist Robby Starbuck has been at the forefront of exposing these divisive efforts, and now he's just called the nation's largest retailer onto the carpet for both their DEI efforts and their sexually charged agenda:\n\nAnti-woke activist and filmmaker Robby Starbuck, who has been leading a campaign exposing major corporations' woke policies, said on X on Monday that he warned Walmart executives last week that he would be doing a story on \"wokeness\" at the retail giant.\n\n\"Instead,\" Starbuck shared, \"we had productive conversations to find solutions.\"\n\nStarbuck outlined the changes Walmart agreed to make, including working to remove sexual and transgender products inappropriately marketed toward children and reviewing grants to Pride events to avoid funding sexualized content targeting kids.\n\nRobby Starbuck has done great work pressuring companies like Walmart, Tractor Supply Co. and John Deere to roll back their problematic DEI policies, but that doesn't mean there aren't some companies out there you'll want to give a miss this holiday shopping season.\n\nThis year, we'd like to make you aware of some virulently antisemitic companies and brands that you might want to think twice about frequenting, many of them in the beauty category. Because the beauty industry is so female-heavy, it's become a haven for the most egregious of leftist policies and often panders to mentally ill men who think they are women, while we regular (and biological!) women are left in the dust.\n\nI wrote about this back in 2017 after despairing at the hostility brewing amongst female beauty bloggers in the wake of Donald Trump being elected. And things have only gotten worse since then, as antisemitic, pro-Hamas \"activists\" have torched their way into the mainstream, particularly in the beauty industry.\n\nHere's who you're going to want to avoid this shopping season:\n\nOwner Huda Kattan, an Iraqi-American raised in Oklahoma City, once said, \"I don't want blood money\" when referring to Israelis and supporters of Israel who purchased her products. That's not all:\n\nIn another post since the Oct. 7 invasion, Kattan wrote that \"Israel, who has the fourth largest army in the world, is NOT the victim, but they repeat the same story and gaslight anyone who comes with facts.\"\n\nIt's clear that she only wants the pro-Hamas crowd as customers. Huda Beauty has found itself right where it should be -- in the crosshairs of the Stop Antisemites movement.\n\nThis one may hurt, as LUSH bath bombs are frequently found on the wish lists of many teens and adults. Here's what happened mere days after the October 7, 2023, massacre of Israelis at the hands of Hamas terrorists:\n\nA backlash has erupted against cosmetics retailer Lush after one of its shops displayed an anti-Israel sign in its window following the Hamas attack.\n\nThe framed sign, which called on passers-by to boycott Israel, appeared in the window of a Dublin store of the British chain.\n\nThis product comes to us via the odious \"supermodel\" Bella Hadid. According to one report:\n\nThe top model and frequent Vogue cover girl is the daughter of Palestinian-born real estate developer Mohammad Hadid and has emerged as an ardent supporter of Palestine's independence.\n\nHadid is also a major fundraiser for relief efforts for the war in Gaza, including significant donations from her personal fortune.\n\nHadid's antisemitism predates the October 7th attack.\n\nAdidas flirted with overt antisemitism earlier this year with its ill-advised release of the \"1972 Olympics shoe,\" complete with an ad campaign featuring the one and only Bella Hadid.\n\nJTA -- Adidas said it will revise a campaign that features Palestinian-American supermodel and activist Bella Hadid modeling a sneaker recalling the 1972 Munich Olympics -- the Games where 11 Israelis died in a terror attack by a Palestinian terrorist group.\n\nYou can't make it up. Even better, Adidas apologized to Bella Hadid for pulling the ad campaign after public outcry.\n\nUnilever\n\nIf anyone has Ben & Jerry's ice cream, which is owned by Unilever, on their wish list this year, get ready to go Grinch on them. These old, antisemitic hippies have been vocal supporters of the Boycott, Divestment and Sanctions (BDS) movement for many years now, going as far as refusing to sell their ice cream in Israel. This now-tarnished brand doesn't deserve space in your freezer.\n\nOkay, now that you know where not to spend your money, here's where you should: right here at RedState.com. We are offering a heckuva Black Friday deal: use code POTUS47 to get 74% off a VIP membership.",
            "source": {
                "uri": "redstate.com",
                "dataType": "news",
                "title": "Redstate"
            },
            "authors": [
                {
                    "uri": "teri_christoph@redstate.com",
                    "name": "Teri Christoph",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.townhall.com/cdn/hodl/2011/329/f8ff010a-1b4c-4797-adba-d3ede98b789d@news.ap.org.jpg",
            "eventUri": None,
            "sentiment": 0.2470588235294118,
            "wgt": 61,
            "relevance": 1
        },
        {
            "uri": "8448655750",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-09",
            "time": "04:22:19",
            "dateTime": "2024-12-09T04:22:19Z",
            "dateTimePub": "2024-12-09T04:22:09Z",
            "dataType": "news",
            "sim": 0.4196078479290009,
            "url": "https://www.bbc.com/news/articles/crmn74m1jkpo",
            "title": "Melbourne synagogue fire 'likely' terror act, police say",
            "body": "Victoria Police say they have no evidence that further antisemitic attacks are planned, but patrols are being increased to reassure the community.\n\nAfter a meeting with Australian Federal Police and domestic spy agency Asio, the state police force said additional \"intelligence\" had led them to conclude the incident should be treated as a probable terror attack.\n\nCommissioner Shane Patton said police had no information before the fire to suggest an arson attack was imminent.\n\nHe declined to provide any further details on the investigation while it continued.\n\nMr Patton's declaration came a day after Prime Minister Anthony Albanese described the incident as \"quite clearly terrorism\" while acknowledging police were still to make up their minds. He called his description a \"personal view\".\n\nOn Monday, state Premier Jacinta Allan said the terror designation meant police would now have extra resources for their investigation.\n\nJewish community leaders have said they believe the attack is an escalation of a recent documented increase in antisemitism in Australia, and that it has heightened fears of violence.\n\nA few worshippers were inside the building at the time of the fire, and have described hearing banging and seeing a window smash, before liquids were thrown inside and lit on fire.\n\n\"The whole thing took off pretty quickly,\" synagogue board member Benjamin Klein, who spoke to witnesses, told The Age newspaper.\n\nAfter officers at the scene were confronted by angry and scared worshippers on Friday, Mr Patton said police were focused on ensuring their safety.\n\n\"We have... extra police officers deployed in those areas where there are high numbers of Jewish persons living and congregating,\" he said.\n\nAllan also called for the city to rally behind its Jewish communities.\n\n\"We cannot let this conflict overseas continue to be a cloak for behaviour like [this].\"",
            "source": {
                "uri": "bbc.com",
                "dataType": "news",
                "title": "BBC"
            },
            "authors": [],
            "image": "https://ichef.bbci.co.uk/news/1024/branded_news/4601/live/05d3c3f0-b5e4-11ef-a2ca-e99d0c9a24e3.jpg",
            "eventUri": "eng-10148238",
            "sentiment": -0.2784313725490196,
            "wgt": 60,
            "relevance": 1
        },
        {
            "uri": "2024-11-554345774",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-23",
            "time": "00:04:29",
            "dateTime": "2024-11-23T00:04:29Z",
            "dateTimePub": "2024-11-23T00:03:54Z",
            "dataType": "news",
            "sim": 0.7803921699523926,
            "url": "https://www.timesofisrael.com/several-dozen-jewish-extremists-in-hebron-try-to-attack-idfs-top-west-bank-commander/",
            "title": "Several dozen Jewish extremists in Hebron try to attack IDF's top West Bank commander",
            "body": "Several dozens Jewish extremists in Hebron for an annual pilgrimage tried to attack the head of the IDF Central Command Maj. Gen. Avi Bluth, who the military said was in the flashpoint West Bank city on Friday to secure the gathering.\n\nFive suspects were arrested by police after they chased Bluth and the soldiers accompanying him, calling the IDF commander a \"traitor.\" The head of Central Command typically has a fraught relationship with settler extremists, since the army is tasked with trying to keep them in check in the West Bank.\n\nThe IDF said that the group of young suspects chased Bluth and tried to block an exit that the military needed for operational activity.\n\nNo injuries were reported to Bluth or the soldiers with him.\n\nAfter five suspects were arrested, the gathering of rioters was dispersed, the army said, adding that it strongly condemned the violence.\n\nEach year, tens of thousands of Jewish worshippers visit Hebron to mark the yearly Torah reading of the biblical Abraham's purchase of\n\nsite where the Tomb of the Patriarch sits to bury his wife, the matriarch Sarah. Successive years have seen Jewish rioters target Palestinian locals whose movement in the city is further restricted by the IDF to secure the area for the pilgrims.\n\nThere was no immediate comment on the attempted attack on Bluth from Prime Minister Benjamin Netanyahu or Defense Minister Israel Katz, the latter of whom earlier Friday announced an end to administrative detention orders for West Bank settlers, meaning Israel will now be using the controversial policy of holding suspects without charge only against Palestinian terror suspects.\n\nThe Shin Bet had reportedly warned against the move, with the security agency's chief Ronen Bar saying in June that banning the measure against Israelis \"will result in an immediate, severe and serious harm to the security of the state\" in cases where there is clear information that a suspect may carry out a terror attack.\n\nAdministrative detention policies allow the Defense Ministry to hold suspects without charge, while administrative restraining orders bar them from visiting certain areas or communicating with certain people. The tool is typically used when authorities have intelligence tying a suspect to a crime but do not have enough evidence for charges to stand up in a court of law.\n\nSettler violence has spiked since the October 7, 2023, Hamas onslaught in the south. Israeli authorities rarely arrest Jewish perpetrators in such attacks. Some rights groups lament that convictions are even more unusual and that the vast majority of charges in these types of attacks are dropped.\n\nBluth pledged \"not [to] blink\" in the face of settler violence when he took over in June as head of IDF Central Command, which oversees the West Bank. His successor, Maj. Gen. Yehuda Fox, said at the time that while \"the vast majority\" of Israeli settlers in the West Bank are \"moral, law-abiding citizens,\" some were \"adopting the ways of the enemy\" and settler leaders weren't denouncing this violence.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [],
            "image": "https://static.timesofisrael.com/www/uploads/2024/11/F240708OBH05-e1732319024799.jpg",
            "eventUri": "eng-10112099",
            "sentiment": -0.3490196078431372,
            "wgt": 58,
            "relevance": 1
        },
        {
            "uri": "8447813612",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-08",
            "time": "11:01:37",
            "dateTime": "2024-12-08T11:01:37Z",
            "dateTimePub": "2024-12-08T11:01:28Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://nypost.com/2024/12/08/us-news/unhinged-man-dubbed-macnazi-waging-war-on-upper-west-side-jews/",
            "title": "Exclusive | Unhinged man dubbed 'MackNazi' terrorizing NYC, ripping down Israeli...",
            "body": "An unhinged, Israel-hating dog walker who lives with his TV-actress sister on the Upper West Side is terrorizing the neighborhood, repeatedly ripping down Israeli hostage posters and allegedly assaulting anyone who dares get in his way, The Post has learned.\n\nSince Hamas' Oct. 7, 2023 terror attack on Israel, Mackenzie Watson - dubbed \"MackNazi\" by many of his neighbors -- has waged a one-man war on anyone posting hostage flyers or removing pro-Palestine stickers, according to court records and some of his alleged victims.\n\n\"He really just hates Jews,\" said a 48-year-old resident who's watched Watson's antics and estimated at least 100 Upper West Siders \"have had bad run-ins with him.\"\n\nShe also said Watson -- who lives in the nabe with his 29-year-old sister Jamie Linn Watson, who's appeared in FX's \"What We Do in the Shadows\" and the Judd Apatow flick \"Please Don't Destroy: The Treasure of Foggy\" -- seems more worried about ripping down posters than caring for the pooches he walks.\n\n\"He'll sometimes have four dogs; they're hooked to his waist, and he's using both hands at the same time to just pull off the stickers at every corner,\" the woman added.\n\nWatson's most recent outbursts include a June incident where he tailed and harassed a 15-year-old girl and her mom, 56, after the teen ripped off one his \"antisemitic\" stop-genocide stickers from a lamp post on the corner of West 103rd Street and West End Avenue, the fearful mother recalled.\n\nWatson then shoved his phone camera in their faces before stalking them for five blocks as they tried to flee him, she said.\n\n\"I don't give a s-t about the hostages, and I don't give a shit about the thousands of dead babies,\" the mom recalled Watson screaming. \"F-k you, piece of s-t! Go f-k yourself! Eat s-t, Zionists! Go kill yourself!\"\n\nThe mother later that day went to the NYPD's 24th Precinct to file a complaint against Watson, only to run into Gary Paul -- another neighbor doing the same thing.\n\nPaul, a 71-year-old architect, told The Post he's had multiple hostile encounters with Watson over the stickers and signage -- at least two of which drove the anti-Israel maniac to follow him multiple blocks.\n\n\"It's not safe for us,\"said Paul.\n\nIn April, Watson sadistically stuck his phone camera in the face of a 45-year-old woman posting stickers raising awareness of Israeli and American hostages taken captive by Hamas -- and screamed in her face \"Zionist bitch! Zionist c -- t!\"\n\nThe woman said she now carries pepper spray in case she ever runs into him again.\n\n\"I shouldn't have to live this way,\" she said.\n\nIn November 2023, he shoved Joseph Goodrich, 32, to the ground, punched him and dislocated his shoulder -- after Goodrich tried to stop the anti-Israel radical from tearing down hostage posters, according to a criminal complaint and the victim's lawyer, Peter Gordon.\n\nWatson was charged with assault, but soft-on-crime Manhattan District Attorney Alvin Bragg's office gave him a slap on the wrist, allowing him in June to plea bargain to a conditional discharge on a lesser charge of second-degree harassment if Watson completed anger management courses and kept out of trouble for a year.\n\nLess than two months later, Watson violated the plea deal by being arrested and charged with allegedly clawing the face and kicking the shin of a 59-year-old man, who intervened in a squabble between him and a woman who objected to the dog walker tearing down a hostage poster on Broadway and West 100th Street, according to the NYPD and a criminal complaint.\n\nThe DA's office charged Watson with assault and harassment and requested a judge void the conditional discharge in the initial assault case, according to court records.\n\nAt his home on Friday, Watson would only say \"there's a genocide going on\" and \"that's what we should be concerned about\" before shutting the door on a reporter.\n\nWatson is among the latest in a long list of New Yorkers who've come under fire since Hamas' terror attack 14 months ago for tearing down Israeli hostage posters and similar signage, including an Adam administration staffer whose job includes bridging \"cultural divides.\"\n\nAfter The Post's expose last week on Nallah Sutherland -- who initially was only required to take multicultural training classes and had a disciplinary note put in her work file -- Mayor Eric Adams intervened and indefinitely suspended her without pay.",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/12/94892922.jpg?quality=75&strip=all&w=1024",
            "eventUri": None,
            "sentiment": -0.3803921568627451,
            "wgt": 58,
            "relevance": 18
        },
        {
            "uri": "2024-11-555276901",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-24",
            "time": "07:26:50",
            "dateTime": "2024-11-24T07:26:50Z",
            "dateTimePub": "2024-11-24T07:26:21Z",
            "dataType": "news",
            "sim": 0.6980392336845398,
            "url": "https://www.timesofisrael.com/liveblog_entry/body-of-missing-chabad-rabbi-found-in-uae-israel-despicable-antisemitic-act-of-terror/",
            "title": "Body of missing Chabad rabbi found in UAE; Israel: 'Despicable antisemitic act of terror'",
            "body": "Emirati authorities have found the body of Rabbi Zvi Kogan, the Prime Minister's Office and Foreign Ministry say in a joint statement.\n\nKogan, a Chabad rabbi in the UAE, had been missing since Thursday.\n\nIsrael's embassy in Abu Dhabi has been in contact contact with Kogan's family in the UAE, says the statement. Family members living Israel have also been updated.\n\nIsrael calls the murder \"a despicable antisemitic act of terror,\" and pledges to use all available means to bring the killers to justice.\n\nKogan is a dual Israeli-Moldovan citizen, and has been part of the Abu Dhabi Chabad chapter since Israel normalized ties with the UAE in late 2020.\n\nKogan is the nephew of Rabbi Gavriel Holtzberg, who was murdered along with his wife in a terror attack at the Nariman Chabad House in Mumbai in 2008, Channel 12 news reported.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [],
            "image": "https://static.timesofisrael.com/www/uploads/2024/11/IMG_6992-copy2.jpg",
            "eventUri": "eng-10112583",
            "sentiment": -0.2784313725490196,
            "wgt": 58,
            "relevance": 1
        },
        {
            "uri": "2024-11-554056605",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-22",
            "time": "16:34:32",
            "dateTime": "2024-11-22T16:34:32Z",
            "dateTimePub": "2024-11-22T16:14:41Z",
            "dataType": "news",
            "sim": 0.6823529601097107,
            "url": "https://edition.cnn.com/2024/11/22/world/israelis-unite-netanyahu-international-arrest-warrant-intl/index.html",
            "title": "Israelis unite behind their prime minister as Netanyahu faces an international arrest warrant",
            "body": "ICC arrest warrant for Netanyahu 'a gut punch' for Israel, says journalist\n\nA decision by the International Criminal Court to issue arrest warrants for Israeli officials was met with anger and annoyance at Jerusalem's bustling Mahane Yehuda Market. But the most palpable sentiment was one of unity.\n\n\"I think it's terrible. What about Putin? What about the real evil people?\" Sarita Katzin Sarfati said about the court's decision to call for the arrest of Israeli Prime Minister Benjamin Netanyahu and former Defense Minister Yoav Gallant for war crimes committed in Gaza after the October 7 attack on Israel last year.\n\n\"Netanyahu is thinking about his people... and I think that all the world should support us and Bibi is our prime minister, and they should support Bibi as well,\" Sarita told CNN, using the Israeli nickname for Netanyahu.\n\nAs shoppers rushed through the narrow alleyways of the market, Netanel Yehuda told CNN he too was outraged.\n\n\"I'm against it. We're a nation, we are independent, and we can take our own decision here. Nobody else can tell us to put someone in jail or anything else,\" he said.\n\nThat sentiment is shared by many in Israel, according to experts.\n\nGil Siegal, a legal scholar at the Ono Academic College in Israel, said The Hague-based court's decision has united Israelis.\n\n\"Israelis come together when under pressure,\" he told CNN. \"We can disagree because we think Netanyahu should do A over B, fine, but when the outer world is coming to get us, so to speak... this external pressure is a uniting force, not a breaking force,\" he said.\n\nMost Israelis still support the war in Gaza, he said, seeing it as a just fight and the only means to keep their country safe. And while many oppose Netanyahu - mass protests calling for his resignation are now happening weekly - most feel he has been targeted unfairly by the ICC.\n\nThe limited opposition to the war is motivated by the rising death toll of Israeli soldiers in Gaza and the hope that a ceasefire would secure the release of the 101 hostages still held there, with the suffering of Palestinians largely absent from the anti-war discourse.\n\nThis is partly because the shock of the brutal October 7 terror attack, during which Hamas-led militants killed more than 1,200 people, is still raw in the country. Many Israelis know someone who was directly impacted by the attack and most have family members or friends who are currently fighting in Gaza or are serving in the military in another capacity.\n\nPortraits of the hostages are on display across Israel, along the sea promenade in Tel Aviv and in the arrivals hall at the country's airport.\n\nSome Israelis are also outraged that the ICC issued warrants for Netanyahu and Gallant alongside one for Mohammed Al-Masri, also known as Mohammed Deif, the Hamas leader who Israel claims was one of the masterminds of the October 7 attack.\n\nThe ICC \"is saying that Gallant and Netanyahu are equal to Mohammed Deif... this is something that Israelis truly cannot comprehend, truly, truly cannot comprehend,\" Siegal said.\n\nYael Vias Gvirsman represents the families of hundreds of Israeli victims of the October 7 attacks at the ICC and was in The Hague on Thursday when the warrants were issued. She said the warrant against Deif was an important recognition \"that Hamas attacks consisted of extermination, torture, rape and other sexual crimes and inhumane treatment\" and that it was good news for families she represents. \"It's the first step for recognition and the first step for them rebuilding their lives,\" she said.\n\nBut she added that the simultaneous warrants against Netanyahu and Gallant were understandably met with \"great shock\" in Israel, \"because it is a nation at its most difficult hour.\"\n\nThe court said it found \"reasonable grounds\" to believe that Netanyahu bears criminal responsibility for war crimes including \"starvation as a method of warfare\" and \"the crimes against humanity of murder, persecution, and other inhumane acts.\"\n\nMore than 43,000 Palestinians have been killed since October 7 last year, according to the health ministry in Gaza.\n\nNetanyahu denounced the ICC move on Thursday, calling it an \"antisemitic decision\" and \"a modern Dreyfus trial,\" referring to the 1894 wrongful conviction of Jewish-French soldier Alfred Dreyfus, an affair that has since come to symbolize antisemitic persecution.\n\nThe prime minister said the ICC judges were \"motivated by antisemitic sentiments against the one and only Jewish state.\"\n\nMeanwhile, opposition leader Yair Lapid called the arrest warrants for Netanyahu and Gallant a \"reward for terrorism.\"\n\nImplications for soldiers fighting in Gaza\n\nWhile the ICC arrest warrants target only Netanyahu and Gallant, some are worried about the implications for the Israel Defense Forces and its soldiers.\n\nConscription is mandatory for most Jewish Israelis and some 300,000 reservists have been called up because of the war, on top of the estimated 170,000 active-duty soldiers.\n\nThe right-wing Israeli legal organization Shurat HaDin has warned about the arrest warrants \"creating a dangerous precedent for the ICC to target other democratic armies and leaders.\" The group has long warned about the ICC possibly opening a criminal investigation against Israeli soldiers.\n\nLegal action at the ICC against Israeli soldiers, it said on its website, would \"carry devastating effects\" on Israel, and cause immediate personal risk to individuals \"whose only blame is for serving their country and fighting terror.\"\n\nRefusals by potential recruits and reservists to serve are rare in Israel, but there are signs that they have been increasing amid the global outrage over the toll of the war in Gaza. Taking an unusually public stance, a group of more than 130 Israeli reservists signed an open letter to Netanyahu and Gallant last month, stating that they refuse to serve unless a deal is signed to end the war and bring back the hostages, saying that for some of them \"the red line has already been crossed.\"\n\nSoul Behar Tsalik, an Israeli who intends to refuse his mandatory enlistment in the IDF next week, said the ICC warrant strengthens his commitment to refuse.\n\n\"Israel's war machine does not only destroy Gaza but also hurts Israelis - in body and in spirit,\" he told CNN. \"I hope the ICC's ruling will help make a change, will make my fellow Israelis realize the truth and severity of the claims against our leaders, and push Israel to leave Gaza, free the hostages and end the occupation as soon as possible.\"\n\nBreaking the Silence, an organization of Israeli veterans who oppose the war in Gaza and the occupation of the West Bank, was a rare voice of support for the ICC's decision.\n\nIt said in a statement that the \"flood of condemnations, an array of whataboutisms and countless allegations of antisemitism\" was indicative of the Israeli \"society's insistence, even now, to not see what we are doing in Gaza.\"\n\nCNN's Michael Schwartz and Kareem Khadder contributed reporting.",
            "source": {
                "uri": "edition.cnn.com",
                "dataType": "news",
                "title": "CNN International"
            },
            "authors": [
                {
                    "uri": "ivana_kottasova@edition.cnn.com",
                    "name": "Ivana Kottasová",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.cnn.com/api/v1/images/stellar/prod/2024-04-26t155038z-1712627661-rc2656a73s4j-rtrmadp-3-israel-palestinians-netanyahu.JPG?c=16x9&q=w_800,c_fill",
            "eventUri": "eng-10105884",
            "sentiment": -0.2941176470588235,
            "wgt": 56,
            "relevance": 1
        },
        {
            "uri": "8465562155",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-19",
            "time": "19:45:33",
            "dateTime": "2024-12-19T19:45:33Z",
            "dateTimePub": "2024-12-19T19:45:07Z",
            "dataType": "news",
            "sim": 0.6745098233222961,
            "url": "https://cbn.com/news/israel/chrismukkah-time-stand-against-antisemitism-bless-israel-and-celebrate-gods-deliverance",
            "title": "'Chrismukkah': A Time to Stand Against Antisemitism, Bless Israel, and Celebrate God's Deliverance",
            "body": "This year, Christmas and the first day of the Jewish festival of Hanukkah coincide on Dec. 25 for a rare alignment of the two celebrations -- unofficially known as \"Chrismukkah.\"\n\nIt doesn't occur often because the dates for Hanukkah vary according to the Jewish calendar.\n\nWhy is it significant this year?\n\nBoth Christmas and Hanukkah celebrate God's deliverance. Christmas, of course, celebrates the Messiah coming to earth as a baby in the manger to save the world from sin and eternal punishment. Hanukkah, also known as the \"festival of lights,\" marks the deliverance of the Jewish people from foreign oppression during the 2nd century B.C.\n\nFast forward more than 2,000 years and the Jewish people again find themselves oppressed and under siege from all sides. The State of Israel is under attack from Iran-backed terror organizations. And Jewish people everywhere face rising antisemitism, including in America where we've seen anti-Israel protests on college campuses and attacks on Jewish students.\n\nAs a Messianic Jew, I believe in Yeshua (Jesus) as Israel's Deliverer, Savior, and Messiah, as foretold in the Old Testament and revealed fully in the New Testament.\n\nIf ever the Jewish people needed divine deliverance and the support of Bible-believing Christians, the moment is now. Israel needs to see that the God of Israel and Yeshua (Jesus) the Messiah, the Babe of Bethlehem and the Deliverer foretold by the Old Testament prophets, is the One who will vanquish their enemies and bring true peace. As Zechariah prophesied, \"It will happen in that day that I will seek to destroy all the nations that come against Jerusalem.\"\n\nJust as Christmas and Hanukkah are \"intertwined\" this year, so is the future deliverance of all those -- Jews and non-Jews -- who believe in Yeshua as Messiah.\n\nAs Messianic Jews, we humbly and gratefully accept the awesome gift of God, the complete deliverance from the eternal consequences of sin that the baby born in a lowly stable in Bethlehem has provided for us.\n\nIt is, therefore, particularly ironic that Bethlehem, the town where Yeshua was born, is not celebrating Christmas this year.\n\nBethlehem: Empty This Christmas?\n\nOngoing conflict in the Holy Land has turned Bethlehem into a virtual ghost town. Typically, at this time of the year, Bethlehem would be bursting at the seams with excited pilgrims, eager to visit the Church of the Nativity and soak in the atmosphere.\n\nBut, this year, the streets are largely deserted. There are no decorations, no festivities, virtually no visitors.\n\nAnd the people of Bethlehem are suffering.\n\nMany struggle to pay for food and other essentials for their children. Anxious parents don't know where to turn. Many see no alternative but to leave Bethlehem -- or stay and face a dire Christmas and desperate winter.\n\nJust as Joseph, the biblical patriarch, prepared to avert a humanitarian disaster in ancient Egypt, the Joseph Project International is staving off hunger and suffering in Bethlehem and across the Holy Land this Chrismukkah.\n\nAs the largest humanitarian aid importer in Israel, the charitable organization has distributed $23 million worth of vital supplies since last year's unprecedented Oct. 7 terror attack, and is helping Jews, Arabs, Muslims, and Christians across Israel and the West Bank (Judea and Samaria), where Bethlehem is located.\n\n\"Many families in Bethlehem are not working due to the decline in tourism,\" says the organization's local operations manager. \"Families (are) simply not able to provide for their kids. Our goal is to support the Christians, encourage them to stay, and renew their peace.\"\n\n'I Will Bless Those Who Bless You'\n\nThis Chrismukkah, as you celebrate Christmas or Hanukkah, remember God promises a special blessing for those who support Israel, speak out against antisemitism everywhere, and stand with God's chosen people:\n\n\"My desire is to bless those who bless you, but whoever curses you I will curse, and in you all the families of the earth will be blessed\" (Genesis 12:3, TLV).",
            "source": {
                "uri": "cbn.com",
                "dataType": "news",
                "title": "CBN.com - The Christian Broadcasting Network"
            },
            "authors": [],
            "image": "https://cbn.com/sites/default/files/media/slider/images/chrismukkahas_hdv.jpg",
            "eventUri": "eng-10189548",
            "sentiment": -0.003921568627450966,
            "wgt": 52,
            "relevance": 1
        },
        {
            "uri": "8467243673",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-20",
            "time": "21:14:14",
            "dateTime": "2024-12-20T21:14:14Z",
            "dateTimePub": "2024-12-20T21:09:34Z",
            "dataType": "news",
            "sim": 0.5058823823928833,
            "url": "https://www.yahoo.com/news/car-drives-crowd-christmas-market-192800388.html",
            "title": "Several dead, about 60 injured when car plows into German Christmas market: Sources",
            "body": "A car plowed into people visiting a Christmas market in Magdeburg, Germany, on Friday, killing several and injuring about 60 others, according to U.S. law enforcement sources.\n\nA suspect has been arrested in the attack that sent shoppers fleeing in panic, the U.S. sources said.\n\nExtensive police operations are underway at the Magdeburg Christmas market, which is now closed, local police said.\n\n\"My thoughts are with the victims and their families,\" German Chancellor Olaf Scholz said. \"We stand by their side and by the side of the people of Magdeburg. My thanks go to the dedicated rescue workers in these anxious hours.\"\n\nMagdeburg is about a two-hour drive west of Berlin.\n\nThis incident comes nearly eight years to the day after a terror attack at a different German Christmas market. On Dec. 19, 2016, a man drove a truck into a crowd at a market in Berlin, killing 13 and injuring dozens.\n\nThe potential for vehicle-ramming attacks is an ongoing concern for U.S. law enforcement officials, especially ahead of New Year's Eve. A joint threat assessment about New Year's Eve in New York City's Times Square noted the use of vehicle-ramming alone or in conjunction with other tactics \"has become a recurring tactic employed by threat actors in the West.\"\n\nThis is a developing story. Please check back for updates.",
            "source": {
                "uri": "yahoo.com",
                "dataType": "news",
                "title": "Yahoo"
            },
            "authors": [],
            "image": "https://s.yimg.com/ny/api/res/1.2/9ne6tPCoYy2iHNO0hq8tFA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD02NzU-/https://media.zenfs.com/en/us.abcnews.go.com/9c005e63291854b2ec9773b34600c53d",
            "eventUri": "eng-10192203",
            "sentiment": -0.2941176470588235,
            "wgt": 51,
            "relevance": 1
        },
        {
            "uri": "8451745351",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-10",
            "time": "22:24:54",
            "dateTime": "2024-12-10T22:24:54Z",
            "dateTimePub": "2024-12-10T22:24:23Z",
            "dataType": "news",
            "sim": 0.4745098054409027,
            "url": "https://www.skynews.com.au/insights-and-analysis/israeli-deputy-minister-of-foreign-affairs-urges-albanese-govt-to-find-its-voice-in-stamping-out-the-scourge-of-antisemitism/news-story/28a1e19624ef65a971565b81bba60fbc",
            "title": "Albanese govt urged to 'find its voice in stamping out the scourge of antisemitism'",
            "body": "Of all the terrible incidents of grotesque antisemitism we have seen around the world since the barbaric massacre in Israel by Hamas on October 7 2023, it is the terror attack on the Adass Israel Synagogue in Melbourne which is the most personally confronting for me.\n\nI spent almost seven wonderful years of my life living in Australia, and despite being born in Canada, Australia is my second home after Israel.\n\nI moved to Australia in 2007 after serving in the Israeli Defence Forces (IDF) during the Second Intifada.\n\nI worked as a veterinary nurse in Bondi and made my home in Sydney - truly one of the most beautiful cities in the world.\n\nLike so many immigrants to your country, I found Australia overwhelmingly welcoming, open, tolerant and free.\n\nAustralia is one of the most successful multicultural nations anywhere in the world, but since October 7, all this has changed.\n\nJew-hate has exploded in Australia; what has happened to the loving, welcoming Australia that made me so happy all those years ago?\n\nThe largest massacre of Jews since the Holocaust has unleashed a torrent of antisemitism in Australia that I never knew existed, and that state and federal governments have clearly failed to adequately deal with.\n\nOn October 8 2023, Sheikh Ibrahim Daoud addressed a protest organised by Hizb ut-Tahrir, delighting in the murder of Jews.\n\nHe said: \"I'm elated. It's a day of courage, it's a day of resistance, it's a day of pride, it's a day of victory.\"\n\nOn October 9 2023, outside the Sydney Opera House, a pro-Hamas mob shouted \"F*** the Jews!\" and \"Where's the Jews?\"\n\nHave any of these people been prosecuted for this hate speech and intimidation towards Jews, no.\n\nJewish students don't feel safe on university campuses around Australia anymore, and a Jewish academic had his office invaded.\n\n\"From the river to the sea, Palestine will be free\" isn't just a chant, it's calling for the destruction of the State of Israel and the slaughter of Jews.\n\nWhy can't university officials understand this and stop the hate directed towards Jewish students?\n\nNear where I used to live in Sydney, cars and other property were recently set alight and then defaced with the most horrific antisemitic messages.\n\nThere was a confrontation between Jews and pro-Palestinian protesters outside the synagogue in Caulfield of my friend Rabbi Daniel Rabin.\n\nAnti-Israel protesters descended on a synagogue in Melbourne in November last year after Jews were Falsely accused of arson.\n\nThere have been several other shocking incidents where Jewish Australians have been pelted with rocks, shoes and eggs.\n\nSome have been spat at, one had a can of drink thrown at him, and many have been abused in the street.\n\nEarlier this year \"a 77-year-old Jewish woman was spat on, threatened and kicked multiple times, by protesters opposing a rally to counter antisemitism, outside the Victorian Parliament House\".\n\nThe Executive Council of Australian Jewry (ECAJ) has done some important work tracking the increase in Jew hate incidents in Australia since October 7.\n\nECAJ Research Director Julie Nathan found that from October 1 2023 to September 30 2024, there were 2,062 anti-Jewish incidents.\n\n\"In the previous 12-month period, ending 30 September 2023, these same bodies logged 495 incidents. Accordingly, there was an increase of 316 per cent in the overall number of reported anti- Jewish incidents compared to the previous year,\" a report stated.\n\nThis is completely unacceptable. The Australian government must do more to combat extreme Jew hate but as Julie Nathan said in her report, \"the response from political and community leaders, university executives and civil society has been tepid at best\".\n\nAs Federal Court Judge Justice Michael Lee recently said in a powerful speech, since October 7 there is a \"stark and discomforting realisation that despite living our whole lives in this country, and thinking we knew it so well, we do not now recognise an aspect of it\".\n\nHe also observed that \"the growth and mainstreaming of antisemitism we have all seen emerge over the last 13 months must be tackled, but understanding how it is to be tackled requires some understanding of how we got to where we are\".\n\nMore leadership is required from the Australian government.\n\nThey have pandered to the anti-Jew mob since October 7 by banning a former Israeli Minister from entering Australia. Ayelet Shaked has similar views to me, will I be banned from Australia too?\n\nThe Australian government is now voting against Israel at the UN.\n\nDoes it surprise anyone that as Justice Lee said, antisemitism is being 'mainstreamed' in Australia when the government says that there should be a Palestinian state without requiring them to recognise our right to exist first, and to release the 101 hostages still held captive by Hamas monster?\n\nAt the time of writing, the perpetrators of the terrorist attack on Adass Israel Synagogue are still at large.\n\nI hope those responsible are caught, prosecuted and severely punished.\n\nAustralia was one of the first nations to vote to support the State of Israel at the UN, we hope we can rely on Australia's support again soon.\n\nAustralia is one of the world's great democracies and multicultural nations.\n\nI just hope the Australian government can find its voice in stamping out the scourge of antisemitism domestically, and to support democracies wherever they are imperilled, like Israel.\n\nIsrael is fighting for its survival against the murderous proxies of Iran who embody the very antithesis of Australian values - it's high time the Australian government recognised this fact and acted accordingly.",
            "source": {
                "uri": "skynews.com.au",
                "dataType": "news",
                "title": "Sky News Australia"
            },
            "authors": [],
            "image": "https://content.api.news/v3/images/bin/3c96e09c862ce0131d07e3c6d6b6fc99",
            "eventUri": "eng-10158467",
            "sentiment": 0.2549019607843137,
            "wgt": 49,
            "relevance": 1
        },
        {
            "uri": "8443434174",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-05",
            "time": "09:51:15",
            "dateTime": "2024-12-05T09:51:15Z",
            "dateTimePub": "2024-12-05T09:51:02Z",
            "dataType": "news",
            "sim": 0.6078431606292725,
            "url": "https://www.legit.ng/nigeria/1628969-afe-babalola-dele-farotimis-arrest-wasnt-alleged-defamation-lawyer-speaks/",
            "title": "Afe Babalola: 'Dele Farotimi's arrest wasn't on alleged defamation', lawyer speaks",
            "body": "PAY ATTENTION: Follow our WhatsApp channel to never miss out on the news that matters to you!\n\nLegit.ng journalist, Ridwan Adeola Yusuf, has over 9 years of experience covering public affairs.\n\nAdo Ekiti, Eikit state - Muhammed Ndakudu Adam, a lawyer, has said technically, the arrest of Dele Farotimi was not on alleged defamation but on refusal to appear in court to defend the alleged defamation.\n\nLegit.ng had reported how a chief magistrate's court in Ado Ekiti, the Ekiti state capital, on Wednesday, December 4, remanded Farotimi, a 'retired' lawyer and activist in prison over alleged defamation of Afe Babalola, a senior advocate of Nigeria (SAN) and founder of Afe Babalola University Ado Ekiti (ABUAD).\n\nFarotimi was seized at an office in Lagos and transported to Ekiti state.\n\nOn Tuesday morning, December 3, the opposition figure, who is vocal on social media, raised an alarm. He alleged that officers attached to the Ekiti state police command had perfected plans to \"abduct\" him from Lagos.\n\nFarotimi accused the command of deploying questionable means to lure him for arrest despite honouring the invitation of Zone 2 police headquarters in Lagos a few weeks ago.\n\nAccording to sources, Farotimi's comments about Babalola were in a book published in Lagos and not Ekiti. The university founder was said to have deemed the former's remarks about him calumnious.\n\nSome persons have described Farotimi's arrest by personnel of the Nigerian police over allegations bordering on libel/defamation as \"a troubling breach of the rule of law.\" But wading into the matter via his verified X (formerly Twitter) handle, Adam made a clarification, saying Farotimi allegedly disobeyed the order of the court to appear.\n\nBarrister Adam said on Thursday, December 4 :\n\n\"From the video Dele made himself, a bench warrant was issued against him and when a bench warrant is issued, it means you have disobeyed the order of the court to appear and defend the allegations against you. So technically, the arrest wasn't on alleged defamation but on refusal to appear in court to defend the alleged defamation.\"\n\nEarlier, Legit.ng reported that activist Aisha Yesufu shared a closed-circuit television (CCTV) footage showing the moment police operatives arrested and took away Farotimi.\n\nYesufu likened Farotimi's arrest to a terror attack and called on Nigerian authorities to prioritise the urgent task of combating the real threats plaguing our nation.",
            "source": {
                "uri": "legit.ng",
                "dataType": "news",
                "title": "Legit.ng - Nigeria news."
            },
            "authors": [
                {
                    "uri": "ridwan_adeola@legit.ng",
                    "name": "Ridwan Adeola",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://cdn.legit.ng/images/1200x675/b3f004ac5c335556.jpeg?v=1",
            "eventUri": "eng-10139280",
            "sentiment": -0.1450980392156863,
            "wgt": 48,
            "relevance": 1
        },
        {
            "uri": "8441334788",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-04",
            "time": "04:32:53",
            "dateTime": "2024-12-04T04:32:53Z",
            "dateTimePub": "2024-12-04T04:32:22Z",
            "dataType": "news",
            "sim": 0.9372549057006836,
            "url": "https://www.zerohedge.com/political/open-borders-have-created-terror-attack-time-bomb-us-2025",
            "title": "Open Borders Have Created A Terror Attack Time Bomb In The US In 2025",
            "body": "If US security was represented as a great dam holding back a historic flood, today it would be a Chinese built Temu dam held together with paper mache and ramen noodles, ready to snap in half and kill a million people downstream. In 2024 there is no security: The public simply operates on blind faith that no one will take advantage of the vast weaknesses built into the system and government officials hide any risks associated with their policies.\n\nBut what are the sources of the danger headed our way? Why is 2025 becoming more and more prominent as an inception date for an attack?\n\nDonald Trump's election win, his impending return to the White House and his promise to close the border and deport millions of illegals could be the cleansing tsunami that America needs, but it could also inversely trigger a host of foreign attacks, domestic attacks as well as False flag events.\n\nHere are the reasons why the next year is ripe for a large scale event...\n\n\"Homeland Security\" is a misnomer; the current head of DHS, Alejandro Mayorkas, openly admitted to a room full of border patrol agents this year that over 85% of illegal immigrants apprehended at the southern border are released into the country. Mayorkas originally claimed the release rate was 70% in an interview with FOX News, only to raise that number to 85% when agents pressed him during the private meeting.\n\nReports indicate that at least 400,000 known criminals have crossed the border illegally during Joe Biden's presidency, and 13,000 of those immigrants were convicted murderers. What we don't know, however, is how many terror suspects and foreign agents have also entered the US in the past four years.\n\nThe DHS releases limited data. Migrants that get a hit on the terror watch list are held and cataloged, of course, but with wide open borders and the Biden White House running interference there's no way to know how many slipped through.\n\nThe political left argues that \"no terror attacks have happened on Biden's watch\", but these are the same people that originally denied the existence of Venezuelan gangs taking over apartment complexes in multiple cities across the country. The saturation of illegal migrants will inevitably lead to a terror event in America, it's only a matter of time. Why? Because now they are under threat of being removed en masse.\n\nWhatever their original plans, the reality of mass deportation puts these people on a time table and some may act out violently in response. Many will feel entitled to stay in the US despite their criminal entry.\n\nIt may not happen on Biden's watch, but his administration will have been the catalyst that made deportations necessary and the resulting attacks possible.\n\nI believe an attack is inevitable in 2025 primarily because of the geopolitical brush fires being ignited across the globe right now. There is also always the looming danger of False flag events designed by covert actors trying to trick the public into placing blame on the wrong culprit.\n\nThe war in Ukraine and the expanding wars in the Middle East involving Israel (and the resurgence in Syria) are dependent on US support and possibly future military involvement on the ground. It's fair to say that without US involvement, all of these wars would end rather quickly. One can debate the ethical necessity of America engaging in proxy conflicts or the need for the US to protect certain allies and assets, but a lot of foreign elements view the US as the root cause of their pain.\n\nThey also know the easiest way to attack the US is through the doorway that the current establishment has left wide open on the southern border.\n\nThe US has been hit with a mass immigration storm while also embroiled in at least two regional proxy wars that have the potential to expand into world wars. Why wouldn't Russia, China, or multiple nations in the Middle East use that weakness to their advantage? Even more disturbing, the globalists that want the US to send troops to defend Ukraine or Israel could also perpetrate an attack that Falsely leads back to Russia or Iran.\n\nI continue to argue that America has no reason to be involved in the majority of foreign entanglements and that we should stay out of these conflicts entirely. But we are where we are. There are malicious people within our own government that want to force Americans into war, and there are foreign actors that hate us because of the actions of these same elites. The dominoes have already been set in motion and guess where that leaves us?\n\nThe conservative sweep on election day means we inherit all the messes that Joe Biden and his handlers created - Economic, political, social, and geopolitical. There will also be considerable motivation for establishment elites to create chaos from thin air while conservatives hold governmental power, and this presents a third domestic threat which will definitely arise in the wake of a Trump presidency: Leftist activists.\n\nThe goal of the progressive establishment when it comes to attacking conservatives is to create so much instability and fear that conservatives feel compelled to set aside their principles and the constitution in order to restore order. In this way the left hopes to \"prove\" that conservatives are the \"fascists\" they often accuse us of being.\n\nFor the past several years conservatives have also been labeled \"domestic terrorists\" bent on civil war, but it's actually the progressive left that engages in the majority of civil unrest and violence in the name of political expediency.\n\nThe first time leftists were enraged by a political loss and took to the streets to riot, most conservatives and even the Trump administration erred on the side of constitutional flexibility. The problem is, leftists have a habit of exploiting free speech rights as a springboard for mob intimidation. Also, most of the riots took place in Democrat controlled states and cities where local officials defended the violence and tried to block any intervention.\n\nSome people argue that leftists are no longer motivated to engage in this kind of unrest and the lack of chaos after Trump's election win is proof. I beg to differ. First, leftists are not a hardy bunch and they tend to wait for warmer weather before going out to cause disruption. Second, Trump isn't even in office yet. Just wait until the mass deportations start and then you'll see all kinds of riots.\n\nThe political left believes that mob violence and looting is a form of free speech and \"reparations\" for perceived injustices. They feel completely justified in their behavior and that makes them exceedingly dangerous. If you see the mass burning of random neighborhoods as an \"ends justify the means\" situation, then you can probably convince yourself that any crime is acceptable.\n\nThis trend of terrorism as activism is likely to evolve beyond simple mobs in the next round. In other words, under a new Trump Administration we should expect smaller Weather Underground-like groups among progressive activists; groups that will engage in terror attacks. The two assassination attempts against Trump this year support this hypothesis.\n\nTo summarize, there are four distinct instigators of political violence all active going into 2025:\n\nThe types of attacks we face comprise a wide spectrum and I fear that conservatives may very well throw support behind a martial law scenario should the situation break out the way I think it will. Infrastructure attacks would be the most devastating (and would not require a high level of effort or sophistication); a lot of people may see military intervention as the best option.\n\nI would argue that this is exactly what the establishment wants. They want the liberty movement to abandon our foundations in the name of security - They want us to take shortcuts that lead us down an authoritarian path. If we are to increase the safety of the American populace it's going to take years of work to fix the mess that progressives have left behind. No shortcuts like martial law.\n\nWe'll have to close the borders tight (The one place where a national guard or military presence makes sense). We'll have to deport millions of illegal migrants already in the country. We'll have to reduce our presence in global proxy wars. We'll have to secure communities through localized efforts (militias).\n\nMost importantly, should violence break out, community participation in defense is paramount. The locals need to be prepared for grid down, for rioting, for random attacks. It's the general public that needs to be ready. Regular civilians are the people that will be there the moment disaster strikes and they must be empowered to take action.\n\nWhen a terror attack takes minutes to achieve, regular people who are there when it occurs have seconds to respond. Until we can repair the damage done to our national security over the past four years, the public is the first and most important line of defense.",
            "source": {
                "uri": "zerohedge.com",
                "dataType": "news",
                "title": "Zero Hedge"
            },
            "authors": [],
            "image": "https://cms.zerohedge.com/s3/files/styles/16_9_max_700/public/2024-12/border-Open1-768x448.jpg?itok=W-x4DmeK",
            "eventUri": "eng-10147968",
            "sentiment": -0.2313725490196078,
            "wgt": 46,
            "relevance": 1
        },
        {
            "uri": "8469054683",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-22",
            "time": "11:28:12",
            "dateTime": "2024-12-22T11:28:12Z",
            "dateTimePub": "2024-12-22T11:27:47Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://nypost.com/2024/12/22/opinion/new-film-on-72-munich-olympics-captures-the-truth-of-terror/",
            "title": "'September 5' film on 1972 Munich Olympics captures the truth about...",
            "body": "It's not cozy Christmas fare, but if you want to see a movie that gets the past half-century of Palestinian terror right, go to a movie theater and see \"September 5.\"\n\nThis compact Paramount release, covering the 1972 Summer Olympics massacre of Israeli athletes in Munich, has a refreshingly simple -- but not simplistic -- take: Kidnapping and murdering civilians is bad, and there is no context in which to justify it.\n\nSwiss-born Tim Fehlbaum, the director, isn't known for ideology; his previous features were science fiction and horror.\n\nIt's the absence of ideology here that works.\n\nWe see the Munich terror attack unfold through the eyes of journalists at ABC Sports -- people who are competent at their job, covering the pre-attack Games, but who aren't foreign-policy \"experts.\"\n\nSo when the ABC team, guided by rookie producer Geoffrey Mason (actor John Magaro), hears gunshots from the athletes' housing compound that September dawn, the reaction is natural, in an era before reporters came to associate global events with terror risk: shock and perplexity.\n\nWhen the terrorists reveal themselves as they peer out of the Israeli athletes' apartment they've taken over, the American journalists reflexively see them as bad people.\n\nThere is no backstory to explain why the terrorists are doing what they are doing, no tales of supposed Israeli oppression.\n\nThe terrorists are fully masked. They brandish guns that they have already used, to kill wrestling coach Moshe Weinberg and weightlifter Yossef Romano. They are silent and scary.\n\nThey don't get to tell their \"side\" in the film, because they have no \"side.\"\n\nIt is so obvious that there is no excuse for such depraved action that no one even thinks to say there is no excuse.\n\nThe sports team keeps the story, beating back an attempt by ABC News to take it over.\n\nThe reporters' first dilemma: What to call the killers on air?\n\nDisregarding an argument that the issue is too complex for a descriptive term, they call them what the Germans are calling them -- terrorists.\n\nIt is clear, too, who the victims are, as the sports team crafts a poster for broadcast, with the nine remaining Israeli hostages' photos and biographies.\n\nIn decades since, we've seen countless similar visualizations of the victims of Islamist terror, including victims of 9/11 and, more recently, Oct. 7. Here, the power is the newness.\n\nAnother now-regular feature of terror attacks that surprises the naïve reporters: government ineffectuality.\n\nThe Munich Olympics were supposed to showcase a reformed, enlightened Germany, and the attack happened partly because West Germany so poorly secured the Games: Elected officials didn't want visuals of armed German officers.\n\nBut it also happened partly because of a post-war innocence -- people didn't think it could happen.\n\nThis was a time before people had to go through body scanners to see a pop star perform, when athletes entering their housing complex could, and would, just hold the door open for strangers.\n\nWhen the German government does figure out what to do, it acts with what the film implies was an impure motive.\n\nAcceding to terrorists' demands to take the hostages to an airfield for an escape to Cairo also conveniently moves the bloody incident away from the Olympics site's concentration of news coverage.\n\nAnd not having to evacuate the Olympics housing altogether means retaining the option, later exercised, to resume the Games.\n\nIt's here that the ABC Sports team screws up, prematurely reporting rumors, encouraged by the German government, that the hostages are all free.\n\nBut Germany's rescue attempt at the Fürstenfeldbruck military base fails, and the terrorists kill all nine remaining hostages.\n\nSportscaster Jim McKay, via archival footage, somberly corrects the mistake on air: \"They're all gone.\"\n\nThe mistake points up the lack of familiarity with evil -- the reporters err partly because they can't conceive of a reality in which the Israelis suffer such a horrific loss.\n\nAmerica was used to happy endings.\n\nThe ABC team in the film doesn't know it, but we do: Sept. 5 was lodged halfway between the end of World War II, 27 years earlier, and 9/11, 29 years later. Twenty-two years after that, we got Oct. 7.\n\nThe joltingly novel aspect of \"September 5\" the film is that, for the sportscasters, it was so new.\n\nOver more than five decades, we've normalized the inconceivable.",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/12/newspress-collage-g2qjul3bq-1734866440853.jpg?quality=75&strip=all&1734848471&w=1024",
            "eventUri": None,
            "sentiment": -0.615686274509804,
            "wgt": 46,
            "relevance": 1
        },
        {
            "uri": "8436208311",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-30",
            "time": "14:14:04",
            "dateTime": "2024-11-30T14:14:04Z",
            "dateTimePub": "2024-11-30T14:13:27Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://expose-news.com/2024/11/30/webcams-in-london-have-gone-dark/",
            "title": "Why have all the live webcams in London gone dark? Does it indicate they are planning a False flag event?",
            "body": "After all London's webcams went dark on Monday, 25 November, Alex Krainer wonders if a False flag attack is being planned on London.\n\nHe suggests that a False flag attack on London may be planned by Western powers to blame on Russia, triggering a whole-of-society mobilisation against Russia. Why, what would they have to gain? Krainer suggests that the Western powers' goal is to maintain their dominance over the Eurasian landmass.\n\nTo complement Krainer's hypothesis, we have added a video released by filmmaker Chris Todd Nolan. Using a series of documentaries he released 7 years ago, Nolan summarises how the Ukraine war really began.\n\nBy Alex Krainer, 27 November 2024\n\nYesterday, as I was finalising my new report about the financial collapse of Great Britain, which is the follow-up to my 26 August article 'The Coming Collapse of Britain', YouTube randomly suggested to me a short video by one Craig Houston titled, 'Why are ALL LONDON webcams offline...?'\n\nWhat? Did I read that right??? I was nearly floored.\n\nMr. Houston searched hundreds of Webcams across London and could not find a single one that was live. See for yourself HERE and HERE! That's extremely odd; clearly, someone had to have made the decision to switch them off - they couldn't all have failed for random reasons.\n\nOne of the webcams over Westminster Bridge displayed the last image it recorded: it was on 2 September at 16:51, which at least gives us a clue about when the Heart of Darkness went dark to the world. However, the reason why someone would decide to cut all the webcams is a mystery.\n\nMr. Houston didn't offer any explanations, which is understandable given that he lives in Britain where singing, \"kung fu fighting,\" or silently praying on the sidewalk can get you arrested. But where he declined to tread, I'll venture a guess, and I think it's the only explanation that makes any sense: they're planning a False-flag terror attack on London which they'll blame on Russia, so that they can trigger an all-out, whole-of-society mobilisation by all of the Western powers against Russia. Now, if this seems far-fetched, there are now several important elements that fit coherently with this scenario, starting with the general geopolitical state of things.\n\nWestern empire and in particular the UK, bet heavily on Ukraine and lost. By now the situation has become as undeniable as it is hopeless. But Western powers aren't showing any inclination to cut and run, like they did from Vietnam in March of 1972 or Afghanistan in August 2021. In spite of facing the world's largest nuclear power with established escalatory dominance in the region and a mobilised, highly trained, motivated and battle-hardened army equipped with devastating conventional weaponry that eclipses anything the West has in its depleted arsenals, they are still escalating. Why?\n\nUkraine is too important and the stakes could not be higher. From the imperial cabal's point of view, the stake is the whole world. In his paper, 'Democratic Ideals and Reality', Sir Halford Mackinder wrote that, \"Who rules East Europe commands the Heartland; who rules the Heartland commands the World-island; who rules the World-island controls the world.\" By World-island, Mackinder meant the Eurasian landmass.\n\nHis theoretical framework remained the foundation of foreign policy for British and American governments to this very day, as we learned from Wes Mitchell, Donald Trump's Assistant Secretary of State for European and Eurasian Affairs as recently as 2018. In a briefing to the US Senate Foreign Relations Committee, he made it explicit that the \"central aim of the Administration's foreign policy is to defend US domination of Eurasian landmass as the foremost US national security interest and to prepare the nation for this challenge.\"\n\nMitchell also said that the Administration was \"working with our close ally the UK to form an international coalition for coordinating efforts in this field.\" These views are not just idle musings of think tanks or academics; the reality on the ground confirms that this is indeed how the imperial cabal regards the outcome of the battle for Ukraine. From the beginning of the war, a few of their lieutenants vented the mindset:\n\nIt is unlikely that the empire's vested interests will quietly accept this \"catastrophe.\" This is why they are escalating provocations against Russia, desperately hoping that the Russians will strike at a NATO member nation, creating the pretext to invoke Article 5 of the NATO Treaty and unleash a unified response where the collective West would confront Russia in a whole-of-society mobilisation effort and hopefully snatch a victory out of the jaws of defeat.\n\nSometimes provocations work and they trigger the intended response. An example was the Pearl Harbour attack, which galvanised the unwilling Americans to join the World War II effort. Another was the attack on RMS Lusitania in 1915, and another the current Ukraine war. But there are circumstances when a galvanising event must be orchestrated to detonate the greater conflict, and the list of known examples through history is very long. Here are just a few cases:\n\nThe examples are very numerous and another one, aimed at triggering World War III against Russia wouldn't be unusual in the context of history. If the population are taken by surprise and genuinely believes the official narratives about the attack, this does invariably create the \"helpful waves of indignation,\" allowing the country's leadership to wrap themselves in the flag, promise justice whatever the cost, and start moving the pieces irreversibly toward military escalation.\n\nI believe that this is the reason why Western powers are encouraging Ukraine to strike into Russia with their missiles, even though there is almost nothing to gain and such escalation clearly makes them the belligerents in the conflict. This is why suddenly, the US is discussing providing Ukraine with nuclear Weapons. They want Russia to respond impulsively, but they know Russia most probably won't take the bait. That's where the False flag comes in, probably in the shape of the detonation of a nuclear weapon in London.\n\nI can't imagine how this could be done. I imagine there's very tight custody chain control with every warhead warehoused by any Western power. But if such weapons were given to Ukraine, that's where the custody chain would end. From there, the warheads could be free to roam and drift back to serve False flag purposes, perhaps on routine military flights, or in ordinary shipping containers. If such a device were detonated from a shipping container, say, on a ship, a train or a truck, some Webcam might catch the event.\n\nBut if all the Webcams were dark, the news could report that it was a Russian missile. And it would be very unlikely that anybody could ever prove otherwise. If such images ever did surface, they'd almost certainly be few and they could be quickly traced and removed from circulation. If there's another coherent explanation for why all of London's Webcams went dark in early September, I can't even begin to imagine it.\n\nTomorrow is Thanksgiving and I considered not sharing the above musings today. For one thing, I could be wrong - that much is obvious. And then it's a downer - nothing to be thankful for. But if I happen to be right ... The one way False flag events can fail is if the public sees through them. False flag attack planners must ambush the people and strike at them from the clear blue skies. A spectacular event like 9/11 will have a powerful impact on people's emotions and in that moment, they'll be susceptible to deceptive narratives and that \"helpful wave of indignation\" will materialise. But if the public is forewarned and expects that a False flag might take place, they'll almost certainly suspect that it was \"an inside job,\" and the attack might blow back into the conspirators' faces. I have therefore decided to take risks with my American readers' long weekend and to also risk embarrassing myself.\n\nIn the thick of the covid-19 pandemic, Dr. Mike Yeadon - one of the true scientists who saw through the hoax and did not fear to speak out about it, said that this is the time to be brave. He wasn't saying that we should go out and tackle police officers or charge against tanks with Molotov cocktails. He was talking about taking the risk of being wrong, of embarrassing oneself. It is easier and safer to be silent about all this.\n\nBut we need to be brave and speak out like our children's future depends on it. Alex Jones predicted the 9/11 attack weeks ahead of time, but back then, his warning sounded so utterly crazy and preposterous that nobody would risk discrediting themselves by sharing Alex's bombshell. In fact, few would even admit to listening to Jones. Few still do. But then again ... if he was wrong, so what? If I'm wrong, nothing happens. If I'm right, however, this information could change history.\n\nI'm not an American citizen, but my children are, so I'll allow myself to do the American thing today and express my profound gratitude for all the subscribers who read these reports which, like today, verge on excessively long. You all came for the signals but I kept you for the sermon. Thank you and Happy Thanksgiving!\n\nAlex Krainer is the founder of Krainer Analytics and creator of I-System Trend Following. He has worked as a market analyst, researcher, trader and hedge fund manager since 1996. Alex was born and raised in a socialist regime of former Yugoslavia, under one-party communist rule.\n\nJust before coming across the article above, we came across the video below posted on Twitter by documentary filmmaker and songwriter Chris Todd Nolan who releases his work through the outlet 'Watchdog Media'.\n\n\"A few years ago, I made a series of documentaries on the war in Ukraine. This relatively short video is a summary of how it really began in 2014. An unelected government began killing its 'own' people in the south-east of the country after visits from Joe Biden and John Brennan,\" Nolan tweeted.\n\nYou can watch Nolan's series of documentaries on the war in Ukraine titled '8 Months in Ukraine' HERE.",
            "source": {
                "uri": "expose-news.com",
                "dataType": "news",
                "title": "The Expose"
            },
            "authors": [
                {
                    "uri": "rhoda_wilson@expose-news.com",
                    "name": "Rhoda Wilson",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://i0.wp.com/expose-news.com/wp-content/uploads/2024/11/FeatNov30b.png?resize=1200%2C720&ssl=1&w=640",
            "eventUri": None,
            "sentiment": -0.1372549019607843,
            "wgt": 46,
            "relevance": 1
        },
        {
            "uri": "8452578059",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-11",
            "time": "11:21:25",
            "dateTime": "2024-12-11T11:21:25Z",
            "dateTimePub": "2024-12-11T11:21:13Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://nypost.com/2024/12/11/world-news/kibbutz-nir-oz-survivor-wants-to-return-home-despite-trauma/",
            "title": "Hamas terrorists burned down her kibbutz, killed her husband and dog...",
            "body": "KIBBUTZ NIR OZ, Israel -- Liat Atzili lost nearly everything on Oct. 7, 2023, when Hamas terrorists rampaged through this kibbutz less than two miles from the Gaza border fence.\n\nTerrorists murdered her husband Aviv Atzili and their dog Revy. They ransacked and burned her home and carried her off as a hostage.\n\nBut Atzili said she's determined to return home to the kibbutz -- despite the devastation and its proximity to the Gaza Strip.\n\nThirty-eight residents of Kibbutz Nir Oz were killed and 75 were kidnapped in the attack. In all, one in four residents was either murdered or taken hostage -- leaving the kibbutz as one of the most devastated communities following the terror attack.\n\n\"I believe that that it's really, really important to bring this place back to life. I think that not doing that is sort of a victory for Hamas, and that coming back here and living here,\" said the US-Israeli citizen, who has family ties to New Jersey.\n\n\"I owe that to myself, to Aviv, to the other people who died protecting the place... I think that that's what they would have wanted. So I'm very committed to it.\"\n\nAtzili was freed after six weeks in captivity as part of the first hostage deal. She has said her captors treated her reasonably well.\n\nThe history teacher also has not lost her optimism that the Israeli-Palestinian conflict can be resolved.\n\n\"I think we don't have a choice,\" she said. \"Really, there are 14 million people living here between the river and the sea, and nobody's going anywhere, so we might as well find ways to live together.\"\n\nMore than a year later, Atzili's home and dozens of others in the community remain in ruins. Her own house was badly damaged by fire, but it remains repairable, she believes.\n\nBefore Kibbutz Nir Oz can rebuild, parts of it must first be destroyed -- homes damaged beyond repair must be demolished so that new ones can be rebuilt.\n\nThe first round of demolition in the community was set to begin Thursday. Atzili figures that it will be at least a year before they can even start rebuilding.\n\nAtzili and other displaced residents of the kibbutz have been living together about 40 miles north in Kiryat Gat. Some of the remaining survivors do not want to return to the beautiful small kibbutz, which is home to a botanical garden and several roaming peacocks.\n\nThey feel the tragedy can never be erased from the village regardless of the amount of new construction -- but they're not yet sure where their new home will be.\n\n\"There are a lot of people in the community who aren't interested in coming back and sort of they haven't been given a civil solution to where they're going to be living in the long term,\" Atzili said.\n\nResidents of the kibbutz earlier had agreed not to take action on the demolitions and rebuilding until after the first anniversary of the attack.\n\nThere are some houses whose fates the kibbutz has not decided, including the home of the Siman Tov family -- all of whom Hamas slaughtered as they huddled together in their safe room.\n\nTheir home remains standing, albeit with the tiled roof caving in. Inside, a few remnants remain of their lives there -- including a metal menorah in a destroyed window sill and children's toys in the front yard. The saferoom where they died still stands, although it is pitch black with smoke and fire damage.\n\n\"Something happened to everybody from the family. Yonatan and Tamar and were shot through the door of their safe room, and they died from their wounds,\" she said. \"Their three children and suffocated from inhaling smoke when the house was set on fire.\"\n\nThe community is internally discussing whether to clean up and leave the home standing as a memorial to the devastating loss, while others do not want the stark reminder of the hell that took place a little more than a year ago, Atzili said.\n\n\"A lot of people know the story and want to see the house,\" Atzili said.\n\nFor Atzili, it is important to return to the community that her husband died trying to protect. He was among three local responders who took on the swath of young terrorists who unleashed evil on the small kibbutz.\n\n\"I want to try to come back here and live here,\" she told The Post. \"But not everybody feels that way, especially people with younger children, which is very, very understandable.\"",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/12/kibbutz-nir-oz-comp-95122897.jpg?quality=75&strip=all&w=1024",
            "eventUri": None,
            "sentiment": -0.3019607843137255,
            "wgt": 45,
            "relevance": 1
        },
        {
            "uri": "2024-12-577875619",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-17",
            "time": "01:34:57",
            "dateTime": "2024-12-17T01:34:57Z",
            "dateTimePub": "2024-12-17T01:28:36Z",
            "dataType": "news",
            "sim": 0.6470588445663452,
            "url": "https://www.abc.net.au/news/2024-12-17/victoria-protest-laws-changes-religion-worship/104734560",
            "title": "Victoria plans protest crackdown in bid to boost social cohesion",
            "body": "The government will also introduce legislation which would establish protest-free zones around places of worship.\n\nThe Victorian government has unveiled broad plans to crack down on protester rights and bolster social cohesion, citing a rise in anti-Semitic incidents across the state.\n\nPremier Jacinta Allan said recent discussions with Victoria's Jewish community in the wake of last month's suspected terror attack on the Adass Israel Synagogue had informed the move.\n\n\"I'll never forget the sight and smell of that blackened synagogue for the rest of my life,\" Ms Allan said.\n\n\"I'll never forget the harrowing stories of those who had escaped from that act of terror.\n\n\"There are too many who want to qualify anti-Semitism or make excuses for it, and I want to make it absolutely clear that I never will.\"\n\nUnder the planned changes announced on Tuesday, the government would introduce laws which it said would more strongly protect the right of people to attend places of worship.\n\nThe changes could include the establishment of safe access areas around places of religious worship to outlaw protests.\n\nMs Allan said the changes would safeguard Victoria's multiculturalism, which was \"the solution\" to social cohesion issues.\n\n\"A modern, multicultural Victoria is one that is built on a simple promise: whoever you are, whoever you pray to, you are safe and welcome in this state,\" she said.\n\nThe premier also announced additional measures to build social cohesion in the state, which she said had clearly deteriorated in recent months.\n\nThe government plans introduce a \"social cohesion pledge\" for multicultural organisations, that must be observed in order to access government grants.\n\nThe proposed legislation will need to pass parliament, and would be formed in discussion with religion leaders and communities.\n\nIt comes as the NSW government vows to make similar law changes, following a rally outside Sydney's Great Synagogue on December 4.\n\nThe government has also earmarked the formation of a new 'Local Escalation and Help' group including representatives of Jewish community groups to liaise directly with government.\n\nProtesters face ban on masks, locks and glue\n\nA separate set of measures were also announced by Ms Allan to deliver greater powers to police when responding to public protests.\n\nUnder the changes, the government would introduce its own state ban on protester use of terror organisation flags, as well as face masks and balaclavas.\n\nWhile acknowledging not all protesters using masks were anti-Semitic, Ms Allan said face coverings had been used by bad actors at protests.\n\n\"We know they are being used to conceal identities, shield agitators from crowd control measures,\" Ms Allan said.\n\nGlue, ropes and locks would also be banned at protests, with the government highlighting protest groups who have used the tools to attach themselves to public spaces.\n\nMs Allan said while the right to protest was important, it would not trump the safety of Victorians.\n\n\"Peaceful protests can and must be protected in this state, protests that harm others cannot,\" Ms Allan said.\n\nPolice given new powers around protests\n\nMinister for Police Anthony Carbines said these new laws would provide an opportunity for Victoria Police to protesters to remove face covering at rallies.\n\n\"Ski-masks are for Mt Buller in the ski seasons, they are not for streets in Melbourne,\" Mr Carbines said.\n\n\"If you stand for something, you don't get to hide behind a mask here in Victoria.\"\n\nMr Carbines said the new laws would mean if a protester refused to remove their face coverings, they could be arrested and charged.\n\nHe said the outlawing of \"attachment devices\" was made in an effort to help emergency services, who faced risks when responding to protesters who used them.\n\nPolice would also be given the power to stop and search people or their vehicles if they suspect they have a dangerous attachment device.\n\nUnder the current law, the government said police had to return such devices to \"offenders\".\n\nUnder the proposed changes, police would be able to seize, remove and destroy the devices.\n\n\"We know that attachment devices that people put first responders at risk in both removing offenders and making a situation safe, they disrupt the economy, they disrupt people from going about their lawful activities,\" Mr Carbines said.",
            "source": {
                "uri": "abc.net.au",
                "dataType": "news",
                "title": "Australian Broadcasting Corporation"
            },
            "authors": [],
            "image": "https://live-production.wcms.abc-cdn.net.au/1611d9387f8c21c811a3252f5c90e868?impolicy=wcms_watermark_news&cropH=714&cropW=1270&xPos=10&yPos=21&width=862&height=485&imformat=generic",
            "eventUri": "eng-10179298",
            "sentiment": 0.03529411764705892,
            "wgt": 44,
            "relevance": 1
        },
        {
            "uri": "8438726855",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-02",
            "time": "14:01:46",
            "dateTime": "2024-12-02T14:01:46Z",
            "dateTimePub": "2024-12-02T14:01:19Z",
            "dataType": "news",
            "sim": 0.6941176652908325,
            "url": "https://www.nbcnews.com/news/world/israel-hamas-war-us-solider-omer-neutra-hostage-idf-dead-rcna182401",
            "title": "Israeli American soldier thought to have been taken hostage now presumed dead, IDF says",
            "body": "TEL AVIV -- An Israeli American soldier who was thought to have been captured alive by Hamas during the Oct. 7, 2023, terror attack was actually killed that day and his body taken into the Gaza Strip, Israel's military said Monday.\n\nOmer Neutra, a 21-year-old New York native, who served as a tank platoon commander after emigrating to Israel, was killed in battle and kidnapped, Israeli Defense Minister Israel Katz said on X, as he paid tribute to the fallen soldier.\n\n\"Omer's life story and dedication represent the best and strongest we have built as a nation,\" he said in a post on X. He added that Neutra fell in battle in Nir Oz, a kibbutz less than two miles from the fenced-off border with Gaza and one of the areas hit hardest when Hamas militants stormed through southern Israel.\n\nHowever, the military did not say how it came to the conclusion over Neutra's death. It added that he had been posthumously promoted to the rank of captain.\n\nAround 250 people were taken hostage during Hamas' terror attacks on Oct. 7, 2023, that also saw 1,200 people killed, according to Israeli tallies. Around 100 people remain in captivity, although a third are believed to be dead.\n\nNeutra was born and raised in the U.S., before he emigrated to Israel as a lone soldier and enlisted in the Armored Corps, according to the Hostages and Missing Families Forum, an advocacy group for those held captive and their families.\n\nIn a statement released today, it said his body was still being held captive by Hamas.\n\nNeutra is survived by his parents, Ronen and Orna, and his brother, Daniel.\n\nIsraeli Prime Minister Benjamin Netanyahu extended his \"heartfelt condolences\" to the family. \"We share in the family's heavy grief,\" he said in a statement, adding, \"We will continue to act resolutely and tirelessly until we return all of our captives -- the living and the dead.\"\n\nNew York Gov. Kathy Hochul, who met with Omer's parents in March, also offered condolences to Neutra's family. \"We pray that his body can be returned to his family who have been speaking out for him & all hostages since that horrific day,\" she said in a post on X.\n\nSpeaking to NBC News' \"TODAY\" in September, Neutra's parents called for a ceasefire and hostage-release deal with Hamas.\n\n\"We basically ask ourselves every morning, 'What are we doing today to try and bring him out?'\" Ronen said, adding that it was \"critical that people do not forget\" the hostages.\n\nNews of Neutra's death came just two days after the mother of Israeli American hostage Edan Alexander told NBC News she was both shaken and relieved to see her son in a Hamas-issued propaganda video.\n\n\"To get this video it's a huge relief for me to see that he's still strong. It was amazing,\" Yael Alexander said in a video call Saturday, hours after the video, captioned \"time is running out,\" was posted on the Telegram channel of Hamas' military wing, the Qassam Brigades.\n\nThe 20-year-old, who appears under duress in the Hamas video, calls on President-elect Donald Trump to use his power to negotiate for the freedom of those who remain in captivity in Gaza.\n\nWhile a fragile ceasefire between Israel and Lebanon's Hezbollah militant group appeared to be holding, there have been few signs of progress in talks to secure a release of the remaining hostages or a cessation of fighting with Hamas in Gaza, where more than 44,000 have been killed in 14 months of war, according to local health officials.\n\nHamas leaders held talks with Egyptian security officials on Sunday to explore ways to reach a deal with Israel that could secure the release of hostages in return for Palestinian prisoners.",
            "source": {
                "uri": "nbcnews.com",
                "dataType": "news",
                "title": "NBC News"
            },
            "authors": [],
            "image": "https://media-cldnry.s-nbcnews.com/image/upload/t_nbcnews-fp-1024-512,f_auto,q_auto:best/rockcms/2023-11/231114-omer-neutra-cs-e9a8e8.png",
            "eventUri": "eng-10135563",
            "sentiment": -0.3490196078431372,
            "wgt": 43,
            "relevance": 1
        },
        {
            "uri": "2024-11-558023814",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "22:04:20",
            "dateTime": "2024-11-26T22:04:20Z",
            "dateTimePub": "2024-11-26T22:01:55Z",
            "dataType": "news",
            "sim": 0.8509804010391235,
            "url": "https://freebeacon.com/campus/enough-is-enough-foxx-introduces-bipartisan-bill-prohibiting-aid-to-universities-that-boycott-israel/",
            "title": "'Enough is Enough': Foxx Introduces Bipartisan Bill Prohibiting Aid to Universities That Boycott Israel",
            "body": "'If an institution is going to capitulate to the BDS movement, there will be consequences,' Foxx says\n\nRep. Virginia Foxx (R., N.C.), the chairwoman of the House Committee on Education and the Workforce, unveiled a bipartisan bill that would prohibit federal aid from flowing to universities that boycott Israel.\n\nFoxx unveiled the measure, the \"Protect Economic Freedom Act,\" alongside Rep. Josh Gottheimer (D., N.J.) on Tuesday. It would amend the Higher Education Act to bar universities that engage in the anti-Semitic Boycott, Divestment, and Sanctions (BDS) movement from receiving federal student aid. Under the legislation, universities must submit annual certifications to the Department of Education, showing they are not engaged in a commercial boycott of Israel.\n\n\"Enough is enough. Appeasing the antisemitic mobs on college campuses threatens the safety of Jewish students and faculty, and it undermines the relationship between the U.S. and one of our strongest allies,\" Foxx said in a statement. \"If an institution is going to capitulate to the BDS movement, there will be consequences -- starting with the Protect Economic Freedom Act.\"\n\nIn the wake of Hamas's Oct. 7 terror attack on Israel, student radicals across the country mobilized to introduce BDS resolutions aimed at compelling their schools to divest from companies with ties to the Jewish state.\n\nWhile the terror-tied Palestinian BDS National Committee says it targets companies implicated in Israel's \"unfolding genocide in Gaza,\" its boycott list includes a who's who of corporate giants. Chevron, for example, is included because it extracts natural gas in Israel. Intel is a target because it maintains research and development centers in the Jewish state.\n\nSome top schools, like Brown University and the University of Michigan, have rejected BDS measures in recent months. Still, more than 30 student governments at universities across the country have passed boycott resolutions, according to the Palestinian BDS National Committee, which counts Hamas, Palestinian Islamic Jihad, and other U.S.-designated terror organizations as members.\n\nThirty-eight U.S. have anti-BDS laws on the books, including Foxx's North Carolina and Gottheimer's New Jersey. For Gottheimer, the new bill is necessary to further \"protect our Jewish community.\"\n\n\"While students and faculty are free to speak their minds and disagree on policy issues, we cannot allow antisemitism to run rampant and risk the safety and security of Jewish students, staff, faculty, and guests on college campuses,\" Gottheimer said in a statement. \"The new bipartisan Project Economic Freedom Act will give the Department of Education a critical new tool to combat the antisemitic BDS movement on college campuses.\"",
            "source": {
                "uri": "freebeacon.com",
                "dataType": "news",
                "title": "Washington Free Beacon"
            },
            "authors": [
                {
                    "uri": "lexi_boccuzzi@freebeacon.com",
                    "name": "Lexi Boccuzzi",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://freebeacon.com/wp-content/uploads/2019/09/GettyImages-451904012.jpg",
            "eventUri": "eng-10124866",
            "sentiment": 0.003921568627450966,
            "wgt": 43,
            "relevance": 1
        },
        {
            "uri": "8425888798",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-23",
            "time": "22:32:11",
            "dateTime": "2024-11-23T22:32:11Z",
            "dateTimePub": "2024-11-23T22:31:13Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.breitbart.com/politics/2024/11/23/javier-milei-announces-argentina-israel-alliance-against-terrorism/",
            "title": "Javier Milei Announces Argentina-Israel Alliance Against Terrorism",
            "body": "President Javier Milei of Argentina announced a new formal alliance with Israel on Thursday, calling it \"a bilateral alliance for freedom, democracy, and against terrorism and dictatorships.\"\n\nThe announcement came the same day as the International Criminal Court (ICC) approved warrants for the arrest of Israeli Prime Minister Benjamin Netanyahu and former Minister of Defense Yoav Gallant, over objections from the United States and Argentina as well.\n\nMilei, an admirer of Israel and the Jewish faith, slammed his predecessors for their closeness to the Iranian regime, which was responsible for a massive terror attack on the AMIA Jewish community center in Buenos Aires in 1994.\n\nHe pledged to support the fight against terrorism, and to stand up for the values of the West against their enemies.\n\nEarlier this year, during a visit to Israel, Milei signed a treaty on social rights with the Israeli government. He also visited Jewish holy sites and the community of Kibbutz Nir Oz, which was decimated by the October 7 terror attack.\n\n\"We will never forget the inhuman attacks with [which] terrorism punished the Argentine people 30 years ago. And we also do not forget barbarism committed by the terrorist group Hamas on October 7th,\" Milei said on Friday.\n\nHe demanded the unconditional release of 101 remaining hostages held by Hamas, including eight Argentinian citizens.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/02/Isaac-Herzog-and-Javier-Milei-at-Kibbutz-Nir-Oz-3--e1707391533419.jpg",
            "eventUri": None,
            "sentiment": -0.2941176470588235,
            "wgt": 43,
            "relevance": 18
        },
        {
            "uri": "2024-12-581034830",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-19",
            "time": "22:02:28",
            "dateTime": "2024-12-19T22:02:28Z",
            "dateTimePub": "2024-12-19T22:01:56Z",
            "dataType": "news",
            "sim": 0.843137264251709,
            "url": "https://www.timesofisrael.com/liveblog_entry/fbi-charges-man-with-attempted-mass-casualty-attack-against-israeli-consulate-in-new-york/",
            "title": "FBI charges man with attempted mass casualty attack against Israeli consulate in New York",
            "body": "Luke Tress is a JTA reporter and a former editor and reporter in New York for The Times of Israel.\n\nNEW YORK -- The FBI has arrested a suspect for an attempted mass casualty terror attack against the Israeli consulate in New York City, according to the consult.\n\nThe suspect, Abdullah Ezzeldin Taha Mohamed Hassan, was an Egyptian national living in Falls Church, Virginia, who instructed an FBI informant to carry out the attack, according to a criminal complaint filed on Monday.\n\nHassan ran several social media accounts that supported ISIS, al-Qaeda and Hamas, and advocated for violence against Jews, the FBI says in the complaint filed in a federal court in Virginia.\n\nLocal police located Hassan after receiving a tip about one of his accounts on X. An undercover FBI asset then connected with Hassan on social media and secure messaging apps, in conversations that took place last month and this month.\n\nHassan instructed the informant on how to join ISIS and shared jihadist propaganda, including a video that advocated for killing Jews. He also encouraged the informant to carry out an attack, sending him instructions on how to create a \"martyrdom video,\" the complaint says.\n\nThe suspect sent the informant bomb-making instructions and told the informant, who said he was in New York, to target a building representing Jews, later settling on the Israeli consulate.\n\nOfir Akunis, Israeli's consul-general in New York, thanks US security services for thwarting the attempted attack.\n\n\"This attempted attack by terror organizations is an attack on the sovereign soil of the State of Israel in its entirety,\" Akunis says in a statement to The Times of Israel.\n\n\"It's proof that terror knows no boundaries and that we must fight it everywhere and every time.\"",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [
                {
                    "uri": "luke_tress@timesofisrael.com",
                    "name": "Luke Tress",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://static.timesofisrael.com/www/images/toi-ln-1200.png",
            "eventUri": "eng-10189659",
            "sentiment": -0.2862745098039216,
            "wgt": 43,
            "relevance": 1
        },
        {
            "uri": "2024-11-560922527",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-29",
            "time": "13:27:57",
            "dateTime": "2024-11-29T13:27:57Z",
            "dateTimePub": "2024-11-29T13:27:11Z",
            "dataType": "news",
            "sim": 0.5921568870544434,
            "url": "https://www.timesofisrael.com/liveblog_entry/senior-uae-official-attends-shiva-for-slain-chabad-rabbi-zvi-kogan/",
            "title": "Senior UAE official attends shiva for slain Chabad Rabbi Zvi Kogan",
            "body": "A representative from the United Arab Emirates attends shiva with the family of Chabad Rabbi Zvi Kogan, who was killed in an apparent terror attack in the UAE last week, Hebrew media outlets report.\n\nDr. Ali Rashid Al Nuaim, a member of the UAE's Federal Supreme Council, attends a shiva in Kfar Chabad, telling family members that the UAE is committed to \"openness and peace,\" and vows that Kogan's legacy will endure.\n\nThe circumstances of Kogan's death have not been disclosed and it is unclear if Emirati authorities have established a motive or where the three suspects were when they were arrested.\n\nIsraeli officials have said Kogan was targeted because he was Jewish and branded his killing as an antisemitic terror attack. Israeli agencies are assisting in the investigation.\n\nKogan had been living in the UAE for several years and had been involved in outreach to the country's Jewish community. He was reported missing on Thursday and his body was discovered on Sunday.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [],
            "image": "https://static.timesofisrael.com/www/images/toi-ln-1200.png",
            "eventUri": "eng-10119195",
            "sentiment": -0.2313725490196078,
            "wgt": 42,
            "relevance": 18
        },
        {
            "uri": "8451854905",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-11",
            "time": "00:43:18",
            "dateTime": "2024-12-11T00:43:18Z",
            "dateTimePub": "2024-12-11T00:43:05Z",
            "dataType": "news",
            "sim": 0.5372549295425415,
            "url": "https://www.bbc.com/news/articles/cdxzqrrrv72o",
            "title": "Australia PM condemns arson incident and anti-Israel graffiti",
            "body": "Authorities in Sydney said they were seeking two people aged between 15 and 20 over the vandalism incident.\n\nThe pair had been wearing \"face coverings and dark clothing\" and were seen running from the scene, New South Wales Police said.\n\n\"We need public assistance to come forward and help identify those two people,\" Commissioner Karen Webb told reporters.\n\nPolice said the car blaze was extinguished shortly after firefighters were called to the scene in Woollahra, a suburb in Sydney's east, at around 01:00 local time (14:00 GMT).\n\nAnti-Israel messages, including \"Kill Israiel\" [sic], were found at the scene, scrawled on the fence of two properties and cars.\n\nAlbanese said he had spoken to the Australian Federal Police (AFP) about the vandalism.\n\nEarlier this week, the law enforcement body established a special taskforce to investigate incidents of antisemitism, including the alleged terror attack in Melbourne, and another vandalism spree that occurred in Woollahra last month. Police do not believe the two incidents in Woollahra are linked.\n\nNew South Wales Premier Chris Minns said the latest incident appeared to have been \"specifically designed\" to \"intimidate the Jewish community in Sydney\".\n\n\"If the question is can we do more? I think the answer is yes, and I'm not closing the door to changes to the law,\" he told reporters, adding that he had spoken with Israel's Ambassador to Australia Amir Maimon.",
            "source": {
                "uri": "bbc.com",
                "dataType": "news",
                "title": "BBC"
            },
            "authors": [],
            "image": "https://ichef.bbci.co.uk/news/1024/branded_news/ffe6/live/85bccaa0-b74a-11ef-ae08-6f18806369d0.png",
            "eventUri": "eng-10161754",
            "sentiment": -0.1058823529411764,
            "wgt": 42,
            "relevance": 1
        },
        {
            "uri": "2024-12-581952304",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-20",
            "time": "18:44:21",
            "dateTime": "2024-12-20T18:44:21Z",
            "dateTimePub": "2024-12-20T18:01:23Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.aol.com/most-anticipated-tv-shows-2024-180123486.html",
            "title": "The Most Anticipated TV Shows of 2024",
            "body": "The Most Anticipated TV Shows of 2024\n\nLucy Ford\n\nDecember 20, 2024 at 7:01 PM\n\nCredit - Netflix (2); HBO; Peacock; Paramount+ with SHOWTIME\n\nCrack the spine of your 2025 planner and start filling in some dates, because we've rounded up all the biggest new and returning shows of next year.\n\n2024 has seen the death of plenty of TV shows, some by design -- like Larry David's long-running Curb Your Enthusiasm, the vampire comedy What We Do in the Shadows, and the most unlikely spin-off hit of all time, Young Sheldon. Then there were those that had the rug pulled out from under them, like the Star Wars series The Acolyte, Netflix's Greek god epic Kaos, and Taika Waititi's fan-favorite Our Flag Means Death.\n\nStill, where some TV doors close, new browser windows open, and next year looks to be packed to the rafters with big-budget swings like a new Game of Thrones prequel and a positively stacked Apple TV+ originals slate, as well as highly anticipated returning faves like The White Lotus, The Bear, and The Traitors.\n\nWe've narrowed down the shows we think will be on everyone's lips in 2025.\n\nBrand new\n\nLockerbie: A Search for Truth (Peacock)\n\nJan. 2\n\nJust days before Christmas in 1988, the UK saw its deadliest terror attack in history when a Pan Am flight was blown up over the small Scottish town of Lockerbie, killing 270 people. In Lockerbie: A Search for Truth, Colin Firth takes on the role of Jim Swire, who lost his daughter in the explosion and became the spokesperson for families who lost loved ones on board. He believes the government is covering up what really happened on the flight, but as 36 years of history reveal, the story is never clear.\n\nAmerican Primeval (Netflix)\n\nJan. 9\n\nIf the title of Netflix's gritty new drama implies something dangerous and evil, well, that's the idea. American Primeval chronicles the birth of the American West, with all the perils and violence that came with warring cultures and religions vying for dominance. Taylor Kitsch leads Peter Berg's series as a traumatized man traversing the terrain, with the always excellent Betty Gilpin as a mother looking for a guide across the country. They hope for freedom, but in the frontier, the best they can ask for may be survival.\n\nThe Pitt (Max)\n\nJan. 9\n\nNoah Wyle as an ER doc? In 2025? It's more likely than you think. The Pitt sees Wyle return to the fluorescent-lit hospital halls as the chief attendant at a Pittsburgh hospital. More 24 than ER, each episode of the series follows one hour in Wyle's 15-hour shift and aims to show the relentless conditions for modern-day healthcare workers in America, from crammed waiting rooms to nursing shortages.\n\nPrime Target (Apple TV+)\n\nJan. 22\n\nAfter the sob-fest that was One Day, we're grateful that Leo Woodall's follow-up series looks to be more adrenaline-spiking than tear-jerking. Prime Target follows Woodall's Edward Brooks, a math genius (hence the reference to prime numbers) on the brink of a major breakthrough who senses someone may be trying to thwart his discovery. He and the FBI agent sent to spy on him (Quintessa Swindell) will attempt to unravel the conspiracy at the heart of both of their work.\n\nWatson (CBS)\n\nJan. 26\n\nIf there are three things that the average TV viewer loves, they are medical dramas, police procedurals, and innovative spins on recognizable IP. Enter Watson, the new series about Sherlock Holmes' doctor sidekick, which bills itself as part medical mystery, part detective show. Morris Chestnut takes the mantle of John Watson (following Lucy Liu's run in the character's last primetime procedural outing in Elementary), who, after the death of Sherlock Holmes, sets up his own practice dedicated to strange and unusual medical issues.\n\nParadise (Hulu)\n\nJan. 28\n\nSterling K. Brown is teaming back up with This Is Us creator Dan Fogleman for this series centered around the murder of the President of the United States (played by James Marsden, always a joy to see pop up in things). Brown plays the head of security, who just so happens to have been the last person to see him alive after being let in on something top secret and potentially world-altering. Cue the intrigue, espionage, gripping mysteries, and Brown doing what he does best: expertly playing a character we don't know whether to root for or against.\n\nSNL 50th Anniversary Special (NBC)\n\nFeb. 16\n\nSNL's birthday bash has been a full-season affair so far, with legacy hosts and returning cast members galore. The actual big five-oh celebration for Lorne Michaels' comedy brainchild will be a three-hour live special dedicated to the sketch show's half-century run. Details so far are thin on the ground, with no word yet on who will take on hosting duties and who from the show's illustrious run will be back for some nostalgic commemoration. Based on the show's 40th anniversary special 10 years ago, we can certainly expect a carousel of big names and multiple musical guests.\n\nZero Day (Netflix)\n\nFeb. 20\n\nZero Day, Netflix's upcoming political thriller, marks Robert De Niro's first step into the world of prestige TV, an impressive feat to hold off on considering so many of his A-list peers have made the jump over the last few years. He'll be joined by Jesse Plemons, Dan Stevens, Lizzy Caplan, and Angela Bassett in the series, about a beloved and former United States president (De Niro, naturally) as he leads the investigation into a catastrophic cyberattack.\n\nThe Americas (NBC)\n\nFeb. 23\n\nMove over David Attenborough, Tom Hanks is coming for your bag. Hanks takes on narrating duties for this expansive docuseries that shows the beauty of nature spanning the most remote parts of both North and South America. The series was filmed over five years, taking viewers from the top of the world in the Arctic to the bottom in the Antarctic.\n\nSuits LA (NBC)\n\nFeb. 23\n\nIf there's one thing that L.A. has in abundance, it's lawyers. So it makes sense that the first spin-off of Suits, the wildly popular, Meghan Markle-starring series about NYC attorneys that became a behemoth streaming hit after it ended in 2019, would decamp for the West Coast. The series stars Stephen Amell as a federal prosecutor from New York who moves to Hollywood to represent some of Los Angeles' most powerful clients. Maggie Grace will also star.\n\nDaredevil: Born Again (Disney+)\n\nMarch 4\n\nIt's been a long, long road to get us to Daredevil: Born Again's release. The long-awaited solo return for Charlie Cox's blind superhero outside of the short-lived Marvel-Netflix partnership was first announced in 2022, but by 2023 it was undertaking a massive creative overhaul with The Punisher's Dario Scardapane brought in as showrunner. The show, which has been billed as a continuation of the character's initial three-season Netflix run rather than a reboot, will bring back series originals Cox, Vincent D'Onofrio as villain Kingpin, and Deborah Ann Woll and Elden Henson as Foggy Nelson and Karen Page to the gritty streets of New York's Hell's Kitchen.\n\nDope Thief (Apple TV+)\n\nMarch 14\n\nDope Thief is another crime novel adaptation set to hit the small screen next year. Top Gun: Maverick screenwriter Peter Craig's 2009 story will star Brian Tyree Henry and Wagner Moura as a duo that runs a grift posing as DEA agents to rob an unknown house in the countryside, only to realize they've stumbled across the biggest narcotics corridor on the East Coast. Ridley Scott will executive produce.\n\nThe Residence (Netflix)\n\nMarch 20\n\nSo far, Netflix's more than $100-million deal with Shonda Rhimes has given us the bodice-ripping behemoth Bridgerton, its spin-off Queen Charlotte, and the Anna Delvey miniseries Inventing Anna. The newest jewel in the crown is The Residence, a murder mystery set within the walls of the White House. Described as an \"upstairs, downstairs, and backstairs\" story, the series stars Uzo Aduba as the eccentric detective alongside Giancarlo Esposito and Randall Park.\n\nThe Studio (Apple TV+)\n\nMarch 26\n\nThe sign of truly making it in Hollywood isn't an award or a mansion in the hills, it's wracking up enough caché to get Martin Scorsese, Ron Howard, Charlize Theron, Zac Efron, and Kathryn Hahn to berate you on screen. The Studio stars Seth Rogen as a movie studio head on the brink of existential crisis as he tries to toe the line between making art and \"movies with a capital M.\" The trailer alone is like a rolodex of big-name cameos playing heightened versions of themselves, which, when executed well, can be delightful.\n\nYour Friends & Neighbors (Apple TV+)\n\nApril 11\n\nJon Hamm as a somewhat sociopathic businessman conning his way through New York? We think we've seen this one before. In Your Friends & Neighbors, Hamm will lead his first TV series since Mad Men and suit back up as a hedge fund manager who, after losing his job and marriage, starts stealing from the wealthy residents of his suburb. Naturally, the con gets out of hand, and when he steals the wrong thing from the wrong house, his new life of petty crime starts to unravel. The series will also star Olivia Munn and Amanda Peet.\n\nGovernment Cheese (Apple TV+)\n\nApril 16\n\nAnother series in Apple TV+'s loaded slate is Government Cheese, starring and executive-produced by David Oyelowo. The surrealist comedy is set in 1969 and revolves around a quirky family in L.A. Oyelowo plays its patriarch who, after being released from prison, tries to curry favor with his wife and kids who resent his absence and have seemingly built a strange life around lofty pursuits and odd hobbies in the time he's been away. The show is created by Paul Hunter, dubbed one of the most influential hip-hop music video directors of all time. Unsurprisingly, early images of the series look gorgeous.\n\nAlien: Earth (FX)\n\nSummer TBA\n\nThe Alien franchise has had a long and storied existence in cinema (the latest installment, Alien: Romulus, came out this year), but Alien: Earth will be its first live-action iteration on TV. They've brought in the big guns for the xenomorph's small-screen debut, roping in Fargo series creator Noah Hawley to helm the (space) ship. The series is a prequel to the original 1979 Ridley Scott film starring Sigourney Weaver and takes place on Earth after a mysterious vessel containing a dangerous entity (three guesses for what it might be!) threatens life as we know it.\n\nStick (Apple TV+)\n\nTBA\n\nOwen Wilson is pitching on the green in Stick, a comedy about golf. He stars as Pryce Cahill, an ex-pro golfer who, after having his career prematurely cut short, becomes the coach for a troubled but talented 17-year-old. If you've seen Eddie the Eagle (2016) or The Karate Kid (1984), you might get a sense of what we're in for. There's still a lot of mystery around this series, but we do know that Timothy Olyphant and Judy Greer will also star.\n\nSmoke (Apple TV+)\n\nTBA\n\nTaron Egerton will team back up with Black Bird creator Dennis Lehane for Smoke, a fictionalized take on the true-crime podcast of the same name about the hunt for an arsonist who seemed to confess their crimes in a novel manuscript. Egerton will star as an enigmatic arson investigator on the hunt for two serial arsonists terrorizing the area. The series will also star Jurnee Smollet, John Leguizamo, and Rafe Spall.\n\nChief of War (Apple TV+)\n\nTBA\n\nJason Momoa wears multiple hats in Chief of War, a series he wrote, executive produced and stars in. It tells the story of the bloody and brutal colonization of Hawaii from the indigenous point of view, and Momoa stars as the warrior Ka'iana, known as the \"most famous Hawaiian in the world.\"\n\nA Knight of the Seven Kingdoms (HBO)\n\nTBA\n\nThe Game of Thrones universe continues to expand its reach. Along with House of the Dragon, 2025 will see another prequel come our way. The series is set 100 years before House of the Dragon's Targaryen turf war and is based on the Tales of Dunk and Egg novellas in George R. R. Martin's original A Song of Ice and Fire series. It revolves around a naive knight, Ser Duncan the Tall, and his squire known as Egg. Martin will write the series and has said it will have a different tone to its successors but it's still Westeros so \"No one is truly safe.\"\n\nChad Powers (Hulu)\n\nTBA\n\n\"Glen Powell Summer\" is extending its run into 2025 with Chad Powers, a comedy series Powell co-created with Michael Waldron based on Eli Manning's character of the same name. Taking inspo from Manning's ESPN docuseries in which he went undercover during college football tryouts, Powell will play a disgraced college quarterback who tries to get a second shot at his big break by disguising himself on a new college team under a different identity (bad wig and prosthetics included!).\n\nThe Four Seasons (Netflix)\n\nTBA\n\nFor those pleading for the return of good old-fashioned classic rom-coms, you may be in luck with The Four Seasons, Tina Fey's remake of the 1981 Alan Alda and Carol Burnett comedy, which was a love story about friendship as much as it was a romance. The story follows three couples who vacation with each other each season, but their harmony is thrown off balance when one of them gets divorced and brings a new partner into the fold. Fey will lead the show and reunite with her Date Night co-star Steve Carrell. Elsewhere in the cast, we have Will Forte, Colman Domingo, Kerri Kenney-Silver, and Erika Henningsen.\n\nIT: Welcome to Derry (HBO)\n\nTBA\n\nThe snapshots of the child-murdering sewer clown Pennywise's history that we got in It (2017) and It Chapter Two (2019) inform the story of Welcome to Derry, the prequel series about Maine's most haunted town. Taking place 27 years before Stephen King's original novel (because Pennywise only shows up in 27-year intervals), the show will explore the town's first sightings and experiences with the dancing clown. Set in the 1960s, expect all the hallmarks of King's penchant for vintage vignettes, including the looming fear of the Cold War as well as whatever monsters live beneath the sewer grates.\n\nLong Bright River (Peacock)\n\nTBA\n\nLiz Moore's novel Long Bright River topped multiple year-end critics lists and was named one of Barack Obama's favorite books of the year when it was released in 2020, so naturally, it is heading to the small screen with an adaptation. Amanda Seyfried will star in the series which follows a beat cop working as the opioid crisis grips the streets of Philadelphia. Her sister, who she's more or less estranged from, battles on the fringes of addiction and the latest danger that sweeps the city, a killer who targets sex workers.\n\nRunning Point (Netflix)\n\nTBA\n\nAfter Mindy Kaling wrapped up her Netflix high school rom-com Never Have I Ever last year, questions turned to where she'd go next. The answer is not very far. She is back with the streamer for her next creation, Running Point, a Kate Hudson-starring series about a woman who inherits the top seat of her family business -- one of the biggest basketball franchises in the country. Sitcom lovers will rejoice at the show's supporting cast, which includes Drew Tarver, of the sublimely hilarious The Other Two, Brenda Song, whose renaissance the internet is cheering on enthusiastically, and Max Greenfield, who's not playing Schmidt from New Girl but who will always be Schmidt in our hearts.\n\nToo Much (Netflix)\n\nTBA\n\nIf you, like seemingly the rest of the world in 2024, decided to rewatch Girls and now yearn for more of Lena Dunham's specific lens on the world of friendship and romance, you're in luck! She's back with Too Much, a series she's written with her husband Luis Felber, about a New Yorker who moves to London after a painful breakup and meets a handsome and kind local. Considering Dunham herself moved from the Big Apple to the other side of the pond and married a hot Brit, we sense there could be some autobiographical license. If the premise wasn't enough, Dunham has roped in Meg Stalter, consistently one of the funniest people on screen (watch Hacks!) and The White Lotus Season 2's hunky nerd Will Sharpe. We're so back, baby!\n\nVictoria Beckham docuseries (Netflix)\n\nTBA\n\nAlthough Netflix's mononymous David Beckham 2023 docuseries focused on the footballer's ascent to \"Golden Balls\" status, it was his wife Victoria, the fashion designer and former Spice Girl, who came out as the real star. The series reminded viewers that behind the pout, Victoria has always had a razor-sharp wit and isn't precious when it comes to joking about herself (as seen in her previous satirical reality show Victoria Beckham: Coming to America). Unsurprisingly, the streamer has jumped on that goodwill and greenlit another series, this time focused on Victoria and her shift from extravagant pop star to quiet luxury fashion mogul.\n\nReturning\n\nThe Traitors Season 3 (Peacock)\n\nJan. 9\n\nThe most gripping reality TV series out there, The Traitors is thankfully returning very early on in 2025. Happy New Year to us! The show where celebrities are pitted against each other in a high-stakes party game of Mafia, in which some are designated secret \"traitors\" who are vying to get others eliminated to steal the top prize, is heading back to the Scottish Highlands with Alan Cumming as host (we would riot if not!) and the likes of Bob the Drag Queen, Chrishell Stause, Dorinda Medley, and Tom Sandoval competing in the mix.\n\nSeverance Season 2 (Apple TV+)\n\nJan. 17\n\nThe wait between Seasons 1 and 2 of Ben Stiller's high-concept workplace drama felt longer than that stretch between 3 p.m. and 5 p.m. at the office on any given Wednesday, but finally, it's upon us. Adam Scott is back as Mark, an employee of Lumon, where employees can separate their work memories from their real-life memories. Season 1 gave us plenty of mysteries about what Lumon is actually up to; let's hope Season 2 gives us some answers before it clocks out for the end of its shift.\n\nThe Night Agent Season 2 (Netflix)\n\nJan. 23\n\nAfter its first season launched as one of the most watched shows in Netflix's history, it was only a matter of time (a month, to be exact) before The Night Agent was greenlit for a second (and third) series. Gabriel Basso's FBI agent Peter Sutherland is back for more explosive twists and turns as he gets further immersed in Night Action, a secret organization full of danger.\n\nMo Season 2 (Netflix)\n\nJan. 30\n\nMo Amer's semi-autobiographical comedy series about his life as a Palestinian refugee in Houston is back for a second season. The show, which is co-created by Ramy Youssef, will pick up with Mo's continued attempts at seeking asylum in the U.S., but in Season 2 he's stranded across the border in Mexico without a passport.\n\nYellowjackets Season 3 (Showtime)\n\nFeb 14\n\nWhat better way to celebrate Valentine's Day than with a bit of survival-based cannibalism? Season 2 of Yellowjackets, the dual-timeline series about a group of teens who got stranded in the wilderness, created even more tension and questions than its first outing. In Season 3, it looks like the team is getting hunted by someone who knows their secret -- but everyone who knows the story is \"us or dead.\"\n\nThe White Lotus Season 3 (HBO)\n\nFeb. 16\n\nThe third installment of Mike White's resort-based murder mystery is one of the most anticipated shows of 2025, especially after the culture-shifting ending of its second season in late 2022. Following from Hawaii and then Italy, this series takes place at the White Lotus branch in Thailand. Naturally, White has cobbled together a killer (literally, perhaps) cast including Parker Posey, Walton Goggins, Jason Isaacs, and Lisa from the K-pop girl group Blackpink.\n\nAndor Season 2 (Disney+)\n\nApril 22\n\nStar Wars spin-off shows haven't had the most success lately, but Andor is a shining jewel among the expansive galaxy's offerings. The show chronicles the events leading up to 2016's Rogue One, with intelligence officer Cassian Andor anchoring the series. While Season 1 took place over a single year, Season 2 will span four years.\n\nThe Handmaid's Tale Season 6 (Hulu)\n\nSpring TBA\n\nIt will have been almost three years since the last season of The Handmaid's Tale by the time Season 6, the show's last, lands in our laps next year, but the creators have promised that the wait will have been worth it. Season 5 left us with an unlikely team-up and an increasingly authoritarian threat in Canada.\n\nThe Bear Season 4 (FX)\n\nTBA\n\nThe Bear's popularity has bubbled over like a pot of boiling water since its debut. Its second season swept every award going and while its third season was met with a more mixed bag of reviews, it's still one of the most talked about shows on TV right now -- not least because it's banging out seasons in a way we haven't seen in decades. Four seasons in four years? We forgot we could live like this!\n\nBlack Mirror Season 7 (Netflix)\n\nTBA\n\nCharlie Brooker's satirical anthology about technology's chokehold on us will be back for a seventh season, so be prepared to start looking at your cell phone or air fryer with some suspicion again. The series will include Emma Corrin, Paul Giamatti, Rashida Jones, Cristin Milioti, and Chris O'Dowd.\n\nThe Buccaneers Season 2 (Apple TV+)\n\nTBA\n\nApple TV+'s answer to Bridgerton is The Buccaneers, the story of five ambitious high-society American women navigating the culture clash of 1870s London. Greg Wise and Leighton Meester will be joining the show's second season.\n\nEuphoria Season 3 (HBO)\n\nTBA\n\nNever has a TBA been more TBA than when it comes to Euphoria, Sam Levinson's dive into the drug-addled, sex-fueled lives of teenagers. While its cast, including Zendaya, Jacob Elordi, and Sydney Sweeney, have entered bonafide Hollywood A-list status since its hiatus began in 2022, Levinson has confirmed that the show will be back for a third season that's due to start filming in January. It's said there will be a time jump from last season, meaning the characters will have aged out of being teenagers.\n\nThe Gilded Age Season 3 (HBO)\n\nTBA\n\nJulian Fellowes' The Gilded Age, set in late-1800s New York, proves that great drama can be found anywhere, even in high-society quibbles over who has the superior opera house. Season 3 will see an evolving New York, where the old guard has been usurped and new socialites run the town.\n\nThe Last of Us Season 2\n\nTBA\n\nThe Last of Us became one of the most popular and gripping shows with its 2023 debut, putting to bed the idea that video games can't be successfully adapted to the screen and solidifying Pedro Pascal's \"Internet Daddy\" status. Season 2 will be based on the game's second installment, Part II, meaning we're time-jumping a few years into the future with Bella Ramsey's Ellie being 19 rather than 14.\n\nPoker Face Season 2 (Peacock)\n\nTBA\n\nRian Johnson has truly cornered the market in whodunits or, as he calls Poker Face, a howcatchem. Natasha Lyonne will return as Charlie Cale, a case-of-the-week Las Vegas detective, pointing fingers at all manner of big-name guest stars. Kumail Nanjiani, Katie Holmes, John Mulaney, Ego Nwodim, and Sam Richardson will all pop by this season.\n\nStranger Things Season 5 (Netflix)\n\nTBA\n\nIt's been so long since Stranger Things' last season that we're almost ready to bring \"Running Up That Hill\" for its second cultural renaissance just to feel something. Still, the wait will hopefully be worth it as we get ready to say goodbye to Hawkins, the Upside Down, and all the characters who are definitely still supposed to be 15-year-olds despite this show nearing its 10th anniversary. After Hawkins gave way to Vecna's destruction last season, the gang will have to pool together one last time to save their town from its biggest villain yet.\n\nWednesday Season 2 (Netflix)\n\nTBA\n\nWednesday Season 1 launched to unprecedented levels of popularity in 2023, usurping Stranger Things' chokehold when it came to streaming numbers. Its second installment has a lot to live up to, but if Jenna Ortega's sardonic take on the classic pigtail-braided character has taught us anything, it's that we should never underestimate The Addams Family (and that black really does look good with everything).\n\nYou Season 5 (Netflix)\n\nTBA\n\nWill Joe Goldberg finally get what's coming to him? That's the question we'll all be asking as we head into You's final season. After murdering his way through New York, California, and London with varying degrees of success, Penn Badgley's stalking serial killer is back on home turf, although this time he's got a multi-millionaire wife to hide behind.\n\nContact us at letters@time.com.",
            "source": {
                "uri": "aol.com",
                "dataType": "news",
                "title": "Aol"
            },
            "authors": [],
            "image": "https://s.yimg.com/ny/api/res/1.2/Ak3eh7cqgBUp9S8JDcZLKg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTEyMDA7aD04MDA-/https://media.zenfs.com/en/aol_time_773/1638770930861b312bd406e463bb6c69",
            "eventUri": None,
            "sentiment": 0.223529411764706,
            "wgt": 41,
            "relevance": 1
        },
        {
            "uri": "8430443612",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "22:10:09",
            "dateTime": "2024-11-26T22:10:09Z",
            "dateTimePub": "2024-11-26T22:09:47Z",
            "dataType": "news",
            "sim": 0.5568627715110779,
            "url": "https://www.factcheck.org/2024/11/viral-claim-Falsely-suggests-trump-ended-violence-in-gaza/",
            "title": "Viral Claim Falsely Suggests Trump Ended Violence in Gaza - FactCheck.org",
            "body": "Este artículo estará disponible en español en El Tiempo Latino.\n\nAttacks by Israeli forces and Hamas continue to kill or displace people in the Gaza Strip. But social media posts misleadingly claim Donald Trump's victory in the presidential election led Hamas to call for an end to the war in Gaza. Hamas has called for a ceasefire several times before the election. And the violence has continued since Election Day.\n\nIsraeli airstrikes killed at least 46 people in the Gaza Strip on Nov. 12. An Israeli attack on a refugee camp school left at least 10 people dead on Nov. 16. And on Nov. 23 the Israeli military issued evacuation orders for a northern Gaza suburb due to rocket fire from Hamas.\n\nAll of this happened after it became clear on Nov. 6 that former President Donald Trump had won a second term in the White House.\n\nBut a claim that arose shortly after the election has continued to spread online, suggesting that Trump's win resulted in an end to the violence in Gaza.\n\nStarting the day after the election, some widely followed accounts posted a screenshot of a headline that said, \"Hamas Calls for 'Immediate' End to War After Trump Election Win.\"\n\nDonald Trump Jr., for example, posted the screenshot on Truth Social and Instagram with the message, \"It took about 12 hours after my father's election win for Hamas to call for peace! @realDonaldTrump isn't even president yet and he's already getting it done. Spectacular.\" Many replies to his post indicated that readers understood it to mean that Trump had ended the war.\n\n\"Trump brings world peace and saves millions of lives and liberals will somehow call him racist,\" one commenter said.\n\nOthers spread similarly suggestive claims without the screenshot, including YouTube influencer and professional boxer Jake Paul, who endorsed Trump's 2024 bid for the White House. On Nov. 7, he posted on X a list titled, \"Trump 48 hours not even in office,\" and included as the third item, \"Hamas calls for 'immediate end to war.'\"\n\nThat claim has continued to spread. Conservative commentator Liz Wheeler posted about it on Nov. 8 and Kayleigh McEnany, who served as press secretary during Trump's first term, repeated the claim on the Nov. 11 episode of her Fox News show, \"Outnumbered.\"\n\nAnd it continues to spread across social media. Another list of Trump's supposed pre-inauguration accomplishments posted to Facebook on Nov. 16 says Hamas has called for an immediate end to the war and claims, \"It has been ONLY 11 days since Donald J. Trump elected, there's already PEACE around the WORLD.\"\n\nBut, of course, Trump's election has not yet ushered in peace in Gaza, and any posts suggesting that it has are wrong.\n\n\"It's impossible for that to be true because the battle is still going on on multiple fronts,\" Ibrahim Abusharif, a professor of journalism and strategic communication at Northwestern University in Qatar, told us in an interview. The fact that the claim is proliferating so widely on social media \"just reminds us again that this is an unreliable space for information, for facts, and for truth telling,\" he said.\n\nThe headline at the root of this claim is real. It appeared on Newsweek's website on Nov. 6. But presenting it on its own, detached from the accompanying story, is misleading since it could be used to suggest that Trump is responsible for ending the violence in Gaza.\n\nThe full story explains that a senior Hamas official told Newsweek: \"The election of Trump as the 47th president of the USA is a private matter for the Americans, but Palestinians look forward to an immediate cessation of the aggression against our people, especially in Gaza, and look for assistance in achieving their legitimate rights of freedom, independence, and the establishment of their independent self-sovereign state with Jerusalem as its capital.\" (As president, Trump proposed a \"realistic two-state solution\" in 2020 with Jerusalem as Israel's \"undivided capital.\")\n\nHamas' calls for an end to the violence aren't new. The group has sought a ceasefire at several points since Israeli forces struck Gaza following the Hamas-led terror attacks on Oct. 7, 2023. Hamas militants killed about 1,200 people in Israel and abducted 254. The Gaza Health Ministry, which is run by the Hamas-controlled government, has reported more than 44,000 people killed in Gaza since the war began.\n\nForecasting what effect the incoming Trump administration may have on the war between Israel and Hamas is difficult, experts agree.\n\n\"Donald Trump's election introduces new uncertainty into Middle East affairs,\" Natan Sachs, director of the Center for Middle East Policy at the Brookings Institution, wrote on Nov. 14.\n\nSachs suggested that the Arab Gulf states and Israel \"may now be eager to give Trump early 'wins,' to capitalize on the relationship for their own interests and in the hope that Trump shows more flexibility as he enters office.\"\n\n\"Trump historically, and those around him, have been very sympathetic to Israel,\" Warren Strobel, the Wall Street Journal's intelligence and security reporter, answered when asked at a panel discussion what the Trump administration would likely mean for the conflict there. \"I think you will see, by and large, support for Israel in the region.\"\n\nStrobel predicted the Trump administration would likely increase its previous maximum pressure campaign aimed at reigning in Iran's nuclear program, largely by imposing economic sanctions, which could affect funding for Hamas and Hezbollah.\n\nHezbollah, a Shiite militant group based in Lebanon and funded largely by Iran, clashed with Israel immediately after Hamas' Oct. 7, 2023, terror attack, leading to a more than yearlong fight on the Israel-Lebanon border. On Nov. 26, 2024, Israel and Hezbollah agreed to a U.S.-brokered ceasefire agreement. The deal does not end the conflict between Israel and Hamas.\n\nIt's unclear exactly what impact Trump's second presidency will have on the war in Gaza.\n\n\"He's fickle,\" Abusharif said of Trump's likely approach. \"He has a history of making muscular promises and not following up.\"\n\nSo we don't know what will happen in Gaza during Trump's next term. But we do know that the fighting continues, regardless of the results of the U.S. election.\n\nAbusharif, Ibrahim. Professor of journalism and strategic communication, Northwestern University in Qatar. Zoom interview with FactCheck.org. 19 Nov 2024.\n\nO'Connor, Tom. \"Hamas Calls for 'Immediate' End to War After Trump Election Win.\" Newsweek. Updated 9 Nov 2024.\n\nNakhoul, Samia, et al. \"Netanyahu calls Hamas ceasefire proposal 'delusional' but Blinken sees scope for progress.\" Reuters. 7 Feb 2024.\n\nMagdy, Samy and Drew Callister. \"Here's what's on the table for Israel and Hamas in the latest cease-fire plan.\" Associated Press. 7 May 2024.\n\nAl-Mughrabi, Nidal and Maytaal Angel. \"Gaza ceasefire: Hamas says again it wants implementation, not more talks.\" Reuters. 13 Aug 2024.\n\nShurafa, Wafaa and Fatma Khaled. \"Death toll in Gaza from Israel-Hamas war passes 44,000, Palestinian officials say.\" Associated Press. 21 Nov 2024.\n\nBrookings Institution. \"How is Trump's reelection likely to affect US foreign policy?\" 14 Nov 2024.\n\nThe Hayden Center (@HaydenCenter). \"New Term, New Challenges: National Security in the Trump Administration.\" YouTube. 20 Nov 2024.",
            "source": {
                "uri": "factcheck.org",
                "dataType": "news",
                "title": "FactCheck.org"
            },
            "authors": [
                {
                    "uri": "saranac_hale_spencer@factcheck.org",
                    "name": "Saranac Hale Spencer",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://cdn.factcheck.org/UploadedFiles/GazaThumb.jpg",
            "eventUri": "eng-10120619",
            "sentiment": -0.3176470588235294,
            "wgt": 40,
            "relevance": 1
        },
        {
            "uri": "8442418205",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-04",
            "time": "17:17:55",
            "dateTime": "2024-12-04T17:17:55Z",
            "dateTimePub": "2024-12-04T17:17:48Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://news.sky.com/story/donald-trump-wants-gaza-ceasefire-deal-by-the-time-he-takes-power-says-qatari-pm-13266834",
            "title": "Donald Trump wants Gaza ceasefire deal by the time he takes power, says Qatari PM",
            "body": "Please use Chrome browser for a more accessible video player\n\nThe man at the centre of negotiations over a Gaza ceasefire has told Sky News Donald Trump wants a deal done before he takes power in January.\n\nSpeaking exclusively to Sky's The World with Yalda Hakim, the prime minister of Qatar expressed cautious optimism but said it required \"maximum pressure\" on all parties to end the fighting.\n\nMohammed bin Abdulrahman bin Jassim al Thani said Mr Trump's advisers and the incoming administration have said they want the situation resolved by his 20 January inauguration.\n\n\"We are trying to coordinate with them our efforts, and all of us, we agree, and we are hoping to get over this situation before the president comes to the office,\" he said.\n\nThe prime minister said the Trump team \"want this to be resolved now - today even\".\n\nMr al Thani also defended Hamas being allowed to continue operating its political office from Doha, Qatar's capital.\n\nHe stressed it was set up \"with full transparency and coordination, and at the request of the US and Israel at that time to have this as to be used as a negotiation platform\".\n\nHe said multiple ceasefires had been brokered through the office since 2014.\n\n\"There are tons of situations where we have prevented an escalation from the beginning in order not to put ourselves in a situation like what we ended up with on 7 October,\" he said.\n\nThe prime minister added: \"There will be always be criticism, a lot of parties who will not like this kind of policy, yes, but it's needed.\"\n\nNegotiations over a Gaza ceasefire have so far proved unsuccessful, with more than 44,500 Palestinians killed in the war, according to the Hamas-run health ministry.\n\nIsrael has vowed to wipe out Hamas after the group killed about 1,200 people and took more than 200 hostages in its October 2023 terror attack.\n\nAbout 100 hostages are still inside Gaza - but at least a third are believed to be dead.\n\nOn Monday, Donald Trump said there would be \"hell to pay\" if the hostages were not released before he re-enters the White House.\n\n\"Those responsible will be hit harder than anybody has been hit in the long and storied History of the United States of America,\" he wrote on his Truth Social site.\n\nSpeaking about what Mr Trump's re-election means for the Middle East - including relations with Iran - the Qatari prime minister said there were \"a lot of risks\" but \"plenty of opportunities\".\n\n\"I hope that everyone sees these opportunities,\" he added.\n\nRead more:\n\nQatar gets gift of state visit but questions remain over rights\n\nQatar threatens to suspend mediation rule in Gaza talks\n\nQatar's emir, Sheikh Tamim bin Hamad al Thani, is currently in the UK for a state visit and a lavish banquet was held in his honour at Buckingham Palace on Tuesday.\n\nThe Gulf state's prime minister told Sky News the trip was a \"celebration\" of long-standing links between Britain and Qatar - and that it was especially welcome as loyalty was \"in short supply in the world\".\n\nHe also addressed criticism of Qatar's human rights record, with some urging Sir Keir Starmer to raise the issue during the visit.\n\nCampaigners have frequently accused it of abuses against migrant workers, curtailing freedom of expression, and discrimination against women and LGBTQ people.\n\nMr al Thani said the wealthy Gulf state was doing its best to address issues.\n\n\"It's unfortunate sometimes when we see all this criticism in human rights or so-called human rights records in Qatar,\" he said.\n\n\"We are not saying that we are a perfect nation or a perfect country, but we are a country that when we see there is something wrong, we acknowledge the facts that these are wrong things, and we are trying to do our best according to our systems and our customs, to modify it and to reform it.\"",
            "source": {
                "uri": "news.sky.com",
                "dataType": "news",
                "title": "Sky News"
            },
            "authors": [],
            "image": "https://e3.365dm.com/24/12/1600x900/0a9b182cbd59a00e7d3ff6dd31414437b50eb040cc6eb09f0359c020aba7e5ca_6766537.jpg?20241204170557",
            "eventUri": None,
            "sentiment": 0.1058823529411765,
            "wgt": 39,
            "relevance": 1
        },
        {
            "uri": "2024-12-567816951",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-06",
            "time": "10:02:25",
            "dateTime": "2024-12-06T10:02:25Z",
            "dateTimePub": "2024-12-06T09:51:02Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.politico.eu/article/terror-attack-bavaria-christmas-market-foiled-terrorism-isis-islamic-state-extremism-far-right-police/",
            "title": "Terror attack on Bavarian Christmas market foiled by police",
            "body": "German authorities foiled a potential terror attack on a Christmas market in Bavaria after a tip-off from a foreign intelligence agency.\n\nThe 37-year-old suspect from Iraq was arrested on Wednesday evening in shared accommodation for asylum-seekers in Augsburg, German newspaper Welt reported. A spokesperson for the Bavarian police confirmed the arrest Friday morning.\n\nWelt, a sister publication of POLITICO in the Axel Springer Group, cited sources saying the suspect had disseminated posts on social media glorifying Islamic State (IS) and photographed the Christmas market in Augsburg. He allegedly talked about wanting to drive a car through the market, according to the report.",
            "source": {
                "uri": "politico.eu",
                "dataType": "news",
                "title": "POLITICO"
            },
            "authors": [
                {
                    "uri": "seb_starcevic@politico.eu",
                    "name": "Seb Starcevic",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://www.politico.eu/cdn-cgi/image/width=1200,height=630,fit=crop,quality=80,onerror=redirect/wp-content/uploads/2024/12/06/GettyImages-2187905725-scaled.jpg",
            "eventUri": None,
            "sentiment": -0.2941176470588235,
            "wgt": 38,
            "relevance": 1
        },
        {
            "uri": "2024-11-553784909",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-22",
            "time": "12:04:45",
            "dateTime": "2024-11-22T12:04:45Z",
            "dateTimePub": "2024-11-22T12:04:16Z",
            "dataType": "news",
            "sim": 0.7921568751335144,
            "url": "https://www.timesofisrael.com/defense-minister-declares-end-to-administrative-detention-against-west-bank-settlers/",
            "title": "Defense minister declares end to administrative detention against West Bank settlers",
            "body": "New Defense Minister Israel Katz announced an end to administrative detention orders for West Bank settlers on Friday, meaning Israel will now be using the controversial policy of holding suspects without charge only against Palestinian terror suspects.\n\nWhile the practice is primarily deployed against Palestinians, it is also used against some extremist Jewish Israelis, which has drawn increasing criticism of the ruling Likud party by far-right coalition members. The measure sees individuals held without charge for up to six months at a time. The detentions can be renewed indefinitely while allowing military prosecutors to keep suspects from being able to see the evidence against them.\n\n\"In a reality where the Jewish settlement in Judea and Samaria is subject to serious Palestinian terror threats and unjustified international sanctions are taken against the settlers, it is not appropriate for the State of Israel to take such a severe measure against the people of the settlements,\" Katz said in a statement, referring to the West Bank by its biblical name.\n\nKatz met with Shin Bet chief Ronen Bar this week and told him that he had decided \"to stop the use of administrative detention orders against Jewish settlers in Judea and Samaria, and asked him to put alternative tools in place,\" Katz's office said.\n\nThe Shin Bet has reportedly warned against the move, with Bar saying in June that banning the measure against Israelis \"will result in an immediate, severe and serious harm to the security of the state\" in cases where there is clear information that a suspect may carry out a terror attack.\n\nAdministrative detention policies allow the Defense Ministry to hold suspects without charge, while administrative restraining orders bar them from visiting certain areas or communicating with certain people. The tool is typically used when authorities have intelligence tying a suspect to a crime but do not have enough evidence for charges to stand up in a court of law.\n\nCurrently, more than 3,400 people, the vast majority of them Palestinians, are being held in administrative detention, according to figures from the Israel Prison Service.\n\nA total of 16 administrative detention orders were issued for Jewish Israelis under former defense minister Yoav Gallant, and seven of them are still being held.\n\nKatz said that \"if there is suspicion of criminal acts, the perpetrators can be prosecuted, and if not, there are other preventive measures that can be taken other than administrative detention orders.\"\n\n\"I condemn any phenomenon of violence against Palestinians and taking the law into one's own hands, and I also appeal to the settlement leadership to take a similar public position and express an unequivocal position on the issue,\" the minister added.\n\nSettler violence spiked after the October 7, 2023, Hamas onslaught in the south. Israeli authorities rarely arrest Jewish perpetrators in such attacks. Some rights groups lament that convictions are even more unusual and that the vast majority of charges in these types of attacks are dropped.\n\nAs recently as this past weekend, dozens of masked settlers set fire to several buildings and a car in the West Bank village of Beit Furik near Nablus, according to the IDF. There has been no news of arrests.\n\nThe defense minister's decision was welcomed by right-wing politicians, with far-right National Security Minister Itamar Ben Gvir, a former settler activist who was previously convicted of terror-related offenses, calling the move \"important and huge news... This is a correction of many years of mistreatment, and justice for those who love the land.\"\n\nFinance Minster Bezalel Smotrich, a settlement advocate, said Katz \"eliminated long-standing discrimination against settlers in Judea and Samaria and put an end to the injustice in which the settlers were second-class citizens and draconian and undemocratic measures were applied against them that trampled on their rights, measures that are not applied against any other population in the State of Israel except terrorists and dangerous enemies.\"\n\nSmotrich clarified that if the \"unacceptable phenomenon\" of settler violence occurs, it \"should be handled by the police and the legal system in accordance with the procedures and rules of evidence of criminal law, just as they would be with any other citizen or population.\"\n\nJustice Minister Yariv Levin congratulated Katz on his decision, calling the move an \"end to discrimination.\"\n\nLevin added that the \"pioneer settlers in Judea and Samaria are overwhelmingly law-abiding. Cases of illegal violence should be handled as is customary with respect to any Israeli citizen and in accordance with the law, as is customary everywhere in the country.\"\n\nMK Simcha Rothman, the chairman of the Knesset Constitution, Law and Justice Committee, welcomed the announcement as a \"moral, just and correct decision.\"\n\nA bill sponsored by Rothman -- which would forbid the use of administrative detention or administrative restraining orders against Israeli citizens, unless they are members of a certain list of terror groups -- is currently making its way through the Knesset.\n\nNot all Israeli politicians supported the move, with MK Gadi Eisenkot, a former IDF chief of staff and current centrist opposition lawmaker, calling it \"a grave and dangerous mistake.\"\n\n\"This is another step toward a severe escalation in Judea and Samaria, for which we will all pay the price,\" Eisenkot warned.\n\n\"The goal of such orders is not law-abiding Jewish citizens but extremist terror elements who tarnish and endanger us as a society,\" he said. \"This step joins other deliberate measures that harm the IDF's ability to fulfill its role as the sovereign authority responsible for the safety and security of residents.\"\n\nHadash-Ta'al MK Ahmad Tibi lambasted the move, saying that \"this is effectively the defense minister's certification of approval for Jewish terror -- a government of terror supporters. Administrative detention applies only to Palestinians. This is yet more proof of the regime of Jewish supremacy. Later, they'll cry about 'antisemitism' in The Hague. In short, administrative detention does not apply to those whose veins flow with blue-and-white blood, members of the 'supreme Jewish race.'\"\n\nThe left-wing Yesh Din human rights nonprofit said that \"administrative detention is a draconian and anti-democratic measure that should be stopped against Palestinians and Israelis alike.\"\n\n\"Instead, law enforcement agencies should conduct effective investigations and bring to justice when there is sufficient evidence to do so. Let us recall that thousands of Palestinians are being held in administrative detention under administrative detention orders that Minister Katz has not revoked,\" the group added.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [
                {
                    "uri": "in_jerusalem@timesofisrael.com",
                    "name": "In Jerusalem",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://static.timesofisrael.com/www/uploads/2024/11/F241107YS231.jpg",
            "eventUri": "eng-10109154",
            "sentiment": -0.3960784313725491,
            "wgt": 37,
            "relevance": 1
        },
        {
            "uri": "8454968780",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-12",
            "time": "19:16:59",
            "dateTime": "2024-12-12T19:16:59Z",
            "dateTimePub": "2024-12-12T19:16:41Z",
            "dataType": "news",
            "sim": 0.6274510025978088,
            "url": "https://www.foxnews.com/world/australian-jewish-community-alarmed-amid-rising-antisemitism-fear-anxiety",
            "title": "Australia's Jewish community alarmed by rising antisemitism: 'Fear and anxiety'",
            "body": "By entering your email and pushing continue, you are agreeing to Fox News' Terms of Use and Privacy Policy, which includes our Notice of Financial Incentive.\n\nA devastating arson attack on a Melbourne synagogue is now being investigated as a possible terror attack, drawing worldwide attention to a stark increase in antisemitism in Australia.\n\nMasked vandals set the Adass Israel Synagogue aflame on Dec. 6, in one of several incidents that have left the Jewish community seeking support from government leaders.\n\nOn Wednesday, Sky News Australia reported a car was destroyed after being set on fire in a Jewish community in Sydney. At least two, but possibly as many as seven, buildings in the area were vandalized, with one graffiti tag reading \"kill Israiel\" (sic). This rash of hate followed in the wake of a similar incident late last month, when vehicles and a restaurant in the same area were covered with graffiti.\n\nFollowing the attacks in Sydney, New South Wales Premier Chris Minns told Sky News Australia, \"Sydney, per capita, has the second-highest number of Holocaust survivors in the world,\" explaining that they came \"to Australia specifically to be free from this kind of hate.\"\n\nJEWISH CHILDREN, TEENS VIOLENTLY ATTACKED IN LONDON: 'STREETS ARE NO LONGER SAFE'\n\nWorshiper Yumi Friedman told Avi Yemini of Rebel News that he was inside the synagogue when he heard banging on the door and saw glass flying. Friedman later said he smelled fire and burned his hand while attempting to open the synagogue door.\n\nFriedman said that responding police told Jewish worshipers to get on the ground and show their hands. \"They came and arrested us,\" he said. \"It took them a while to realize that we're Jewish and we didn't do this.\"\n\nZionism is not a feature of the Haredi Judaism that worshipers at the Adass Israel Synagogue practice. Yemini asked members of the community why they believed the non-Zionist synagogue was targeted. \"Jews are Jews,\" a man wearing a kippah replied. \"They're anti-Jews,\" another visibly Jewish man told Yemini. \"Not anti-anything else.\"\n\nYemini filmed a protester outside the firebombed synagogue wearing a keffiyeh and a baseball cap featuring the Palestinian flag who held a sign stating \"Nothing is more antisemitic than Zionism.\"\n\nNumerous community members interviewed by Yemini said they felt unsupported by the local government. \"People have been attacked here,\" one man reminded Victoria Police Detective Inspector Chris Murray, who was present to address the community. \"Why don't you put someone in here?\"\n\n\"We're doing our best,\" Murray responded.\n\nMurray told crowds that police would \"do everything\" to \"bring these individuals before the courts.\" Though they believed the attack was targeted, Murray said that \"what we don't know is why.\"\n\nShane Patton, Victoria police chief commissioner, told reporters at a press conference that the firebombing is being investigated as \"a likely terror attack.\"\n\nCALLS FOR US TO DO MORE AS ANTISEMITIC ATTACKS SKYROCKET IN EUROPE: 'ENORMOUSLY PAINFUL'\n\nPrime Minister Anthony Albanese has been lambasted for his response to the Melbourne attack, which a Sky News Australia host said was \"four days too late.\" Yemini documented Albanese's visit to the Adass Israel Synagogue. When the kippah-wearing prime minister failed to answer questions from assembled reporters, Yemini followed him to the car, telling Albanese that \"yesterday was the first time you didn't conflate antisemitism and Islamophobia.\"\n\nThough it has faced more intolerance, the Jewish population of Australia is around one-eighth the size of the Muslim population, and has been stagnant or declining while the percentage of Muslims has grown. In 2016, Jewish Australians made up 0.5% of the population, according to Monash University. Muslims made up 2.6% of the population in 2016, according to the University of South Australia. Today, Muslims account for 3.2% of the Australian population while 0.4% of the population is Jewish.\n\nIn the aftermath of recent attacks, Albanese stated that the Australian Federal Police will be conducting an operation that would \"focus on threats, violence, and hatred\" targeting the Jewish community. Reuters reported that Albanese has allocated $25 million (approximately U.S. $15 million) since 2022 to increase security for Jewish organizations. He has also worked to minimize hate speech and banned the Nazi salute.\n\nMany Jewish Australians believe these efforts are not enough. Earlier this month, the Executive Council of Australian Jewry (ECAJ) sent an open letter to Albanese, which it shared with Fox News Digital. The ECAJ explained that \"the very character of this country as a free, democratic and multicultural society is in peril,\" citing the \"fear and anxiety\" experienced by Jewish Australians who question whether it is safe to display signs of their Judaism or publicly celebrate their faith and heritage.\n\nThough the ECAJ expressed gratitude to Albanese for \"swiftly condemning\" the arson in Melbourne, they requested that he act in response to \"what is now a national antisemitism crisis.\" Among their requests are an increase in security funding, support for antisemitism education in schools, enforcement of laws against harassment and intimidation, and support for higher government efforts to curtail antisemitism in universities.\n\nCOLUMBIA GROUP'S ANTISEMITIC NEWSPAPER DRAWS OUTRAGE FROM NY LAWMAKER, AS UNIVERSITY INVESTIGATES\n\nAlbanese's office did not respond to Fox News Digital's request for comment about criticisms of the prime minister's reaction to the Melbourne firebombing, his response to the ECAJ's letter, and whether the country's shift regarding a Palestinian state might have an impact on the state of antisemitic hate in Australia.\n\nAs it has worldwide, antisemitism has risen dramatically in Australia since Oct. 7, according to an ECAJ report from November 2024. Reporting entities counted 2,062 antisemitic incidents in Australia between Oct. 1, 2023, and Sept. 30, 2024, compared with 495 incidents tallied during the prior 12 months. This represents a 316% increase in expressions of anti-Jewish hate, which began as early as Oct. 8, when the ECAJ reported that Sheikh Ibrahim Daoud told an audience in western Sydney that he was \"elated,\" explaining, \"it's a day of pride, it's a day of victory.\"\n\nThe ECAJ sent Fox News Digital a trove of photographs showing acts of hate directed against Jewish Australians. These included an incident from November 2023, when unknown individuals sprayed \"Kill Jews\" and \"Jew lives here\" on a residential unit in southeast Melbourne, and wrote \"Jew-free zone\" in a Brunswick window, as reported by the Jewish Independent.\n\nThe government responded to some major acts of antisemitism. In February, anti-Israel activists released a document featuring the \"names and other personal details\" of 600 Jewish musicians, writers, academics and artists in a WhatsApp group whose communications were also leaked.\n\nSeven months later, Attorney-General Mark Dreyfus announced a proposed sentence of up to six years in prison for those who release individuals' private details in order to cause harm. The punishment would increase to seven years if a victim was targeted because of their race, religion or sexual orientation, among other factors.\n\nIn recognition of the rising intolerance in Australia, on Dec. 9, the Simon Wiesenthal Center issued a travel advisory warning Jews to \"exercise extreme caution\" if visiting the country. As Rabbi Abraham Cooper, the center's director of global social action, explained, authorities there have failed \"to stand up against persistent demonization, harassment and violence against Jews and Jewish institutions in Australia.\"",
            "source": {
                "uri": "foxnews.com",
                "dataType": "news",
                "title": "Fox News"
            },
            "authors": [
                {
                    "uri": "beth_bailey@foxnews.com",
                    "name": "Beth Bailey",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2024/12/1024/512/gettyimages-2188481636.jpg?ve=1&tl=1",
            "eventUri": "eng-10158467",
            "sentiment": -0.2862745098039216,
            "wgt": 37,
            "relevance": 18
        },
        {
            "uri": "8466644853",
            "lang": "hin",
            "isDuplicate": False,
            "date": "2024-12-20",
            "time": "12:50:02",
            "dateTime": "2024-12-20T12:50:02Z",
            "dateTimePub": "2024-12-20T12:49:18Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.dnaindia.com/hindi/india/news-what-does-the-police-theory-say-in-atul-subhash-suicide-case-from-unwilling-marriage-to-suicide-many-revelations-4144320",
            "title": "अतुल सुभाष सुसाइड केस में क्या कहती है पुलिस की थ्योरी, बेमन शादी से लेकर आत्महत्या तक, कई खुलासे",
            "body": "अतुल सुभाष सुसाइड केस में क्या कहती है पुलिस की थ्योरी, बेमन शादी से लेकर आत्महत्या तक, कई खुलासे\n\nघर पहुंचा पार्सल, अंदर लाश देखकर उड़े होश, भेजने वाले ने मांगी 1.3 करोड़ की रंगदारी, पढ़ें पूरी बात\n\nDiabetes Management: इन 7 बातों का ध्यान रखें डायबिटीज के मरीज, कभी नहीं बढ़ेगा शुगर लेवल\n\nIND VS AUS BOXING DAY TEST: जानिए भारत का बॉक्सिंग डे टेस्ट में कैसा रहा है रिकॉर्ड? 26 दिसंबर को ऑस्ट्रेलिया से होगा सामना\n\nबांग्लादेश में हिंदुओं के खिलाफ हिंसा के 2,200 और पाकिस्तान में 112 मामले, सरकार ने जारी किए चौंकाने वाले आंकड़े\n\nUGC NET December 2024: यूजीसी नेट का टाइम टेबल जारी, जानें किस डेट को होगा किस सब्जेक्ट का एग्जाम\n\nसर्दियों में सेहतमंद रहने के लिए रोज खाएं ये फल, मौसमी बीमारियां रहेंगी कोसों दूर\n\nPalmistry: हथेली में इन 3 रेखाओं के मिलने से बनती है धन की कोठरी, जानें क्या मिलता है संकेत\n\nअडानी समूह की बड़ी सौगात, 20000 करोड़ का निवेश, अब यहां पावर प्लांट लगा देंगे 12000 नौकरियों के मौके\n\nDelhi News: भाजपा हेडक्वार्टर के बाहर मिला संदिग्ध बैग, इलाका सील, बम स्क्वॉयड बुलाया गया\n\nकितना बदल गया है TV का 'राम', तस्वीर शेयर करते ही हिला दिया पूरा इंटरनेट\n\nViral News: अश्विन ने रिटायरमेंट के बाद खोले बड़े राज, फोन का कॉल लॉग साझा कर कहा-मुझे दिल का दौरा पड़ जाता\n\nबहराइच में दिल्ली के कंझावाला जैसा केस, तहसीलदार की गाड़ी से टकराकर 30 किमी घिसटा युवक, उड़ गए चिथड़े\n\n'पंजाबी झुकेगा नहीं', Diljit Dosanjh ने अब महाराष्ट्र सरकार पर निकाली भड़ास, मुंबई कॉन्सर्ट से जुड़ा है मामला\n\nBhopal News: जंगल में खड़ी कार से निकला 52 किलो सोना, IT रेड करने वाली टीम भी खजाना देख दंग\n\nWinter Skin Care: सर्दियों में क्यों फटने लगती है स्किन? जानें कारण और बचाव के लिए घरेलू उपाय\n\nAtul Subhash Suicide: पत्नी निकिता ने अतुल सुभाष को बताया अय्याश, 'एक साथ 3 लड़कियों संग...'\n\nUP: मेरठ में भी हाथरस जैसी भगदड़, प्रदीप मिश्रा की कथा में बेकाबू हुई भीड़, कई बच्चे-महिलाएं कुचले\n\nSA Vs PAK ODI: पाकिस्तान ने वनडे सीरीज जीतने के लिए की चीटिंग? क्लासेन के दावे से सनसनी\n\nGaza में युद्ध विराम होगा या नहीं? Netanyahu ने अपना फैसला सुना दिया है!\n\nझुर्रियों को अब कहें अलविदा, इस पाउडर के इस्तेमाल से पाएं चांद जैसी चमकदार त्वचा\n\nOm Prakash Chautala Death: पढ़ने का ऐसा जज्बा कि तिहाड़ जेल से दिया एग्जाम, कितने एजुकेटेड थे ओमप्रकाश चौटाला?\n\nDigvijay Rathee होंगे Bigg Boss 18 के मिड वीक में एलिमिनेट? फैंस को लगा झटका\n\nZika Virus ने फिर बढ़ाई लोगों की चिंता, देश के इस राज्य से सामने आया नया मामला\n\nदिल्ली-नोएडा DND फ्लाईवे पर टोल वसूली रहेगी बंद, सुप्रीम कोर्ट ने इलाहाबाद हाई कोर्ट का फैसला ठहराया सही\n\nStree 2 से लेकर Bhool Bhulaiyaa 2 तक, 2024 में सबसे ज्यादा पॉपुलर हुईं ये 10 फिल्में\n\nहरियाणा के पूर्व सीएम ओमप्रकाश चौटाला का निधन, 89 साल में ली आखिरी सांस\n\nBhanu Saptami 2024: इस दिन है साल की आखिरी भानु सप्तमी, जानें सही तारीख से लेकर पूजा विधि और धार्मिंक महत्व\n\nIndian Airforce में अग्निवीरों की बंपर भर्तियां, जानें कौन कर सकता है आवेदन\n\nसेहत का खजाना है एवोकाडो, डाइट में शामिल करने से मिलेंगे ये चमत्कारी फायदे\n\nGood News: बेझिझक अंडा खा सकेंगे Cholesterol के मरीज, वैज्ञानिकों ने खोज निकाली नई तरकीब\n\nJaipur Petrol pump Blast: कैसे हुआ जयपुर में इतना बड़ा हादसा? CNG धमाके ने छीन ली कई जिंदगियां, जानें पूरी स्टोरी\n\nTeeth Sensitivity Remedies: ठंडा-गर्म खाने पर होती हैं दांतों में झनझनाहट, डेंटिस्ट के पास जाए बिना दूर कर सकते हैं समस्या\n\nIran के सुप्रीम लीडर खामनेई ने महिलाओं को बताया फूल, तो इजरायल ने क्यों याद दिलाई इस महिला की?\n\nपत्नी Aishwarya को प्रोटेक्ट करते दिखे अभिषेक बच्चन, तलाक की अफवाहों के बीच वायरल हुआ वीडियो\n\nमहाराष्ट्र के 3 हिल स्टेशन छुट्टियों के लिए सबसे खास डेस्टिनेशन\n\nFrizzy Hair की समस्या को ऐसे करें दूर, हेयर केयर के दौरान इन 5 बातों का रखें ध्यान\n\nViral: जानलेवा बना सेल्फी लेना, अचानक पीछे से आ गई ट्रेन फिर जो हुआ वह बेहद खतरनाक, देखें Video\n\nUP: हर हफ्ते 40 हजार कमाने का लालच देकर छात्रा को बुलाया मुंबई, अश्लील वीडियो बनाकर किया वायरल\n\n'कानून महिलाओं की भलाई के लिए है, पति को सताने के लिए नहीं', तलाक केस की सुनवाई के दौरान सुप्रीम कोर्ट का बड़ा बयान\n\nWinter Session: फिर छिनेगी Rahul Gandhi से सांसदी? बीजेपी सांसद ने दिया नोटिस, निलंबन की मांग\n\nPollution: दिल्ली की हवा में फिर से घुला जहर, स्कूल और दफ्तरों में लागू हुआ हाइब्रिड मोड, 450 के पार पहुंचा AQI\n\nCAT 2024 Results जारी, जानें नतीजों के बाद अब आगे क्या करना होगा\n\nVastu Tips: भूलकर भी किसी के घर से न लाएं ये 3 चीजें, हंसते खेलते परिवार में आ जाएगा तूफान\n\nसर्दियों में मक्के से रिप्लेस करें गेहूं का आटा, एक-दो नहीं, पूरे 5 फायदे देगी मक्के की रोटी\n\nPushpa 2 के डायरेक्टर Sukumar ने की भगदड़ में घायल बच्चे से मुलाकात, पैसों से की परिवार की मदद\n\nकौन है इस 'दिव्य' भैंस का मालिक?, दो गांवों के बीच मची लड़ाई, अब DNA टेस्ट कराएगी पुलिस, बड़ा ही दिलचस्प है ये केस\n\nViral: पुनीत सुपरस्टार प्लेन से आ रहा था बाहर, शख्स ने जड़ दिया थप्पड़, Video देख लोग बोले- हर जगह मार खाता रहता है\n\nUP: बिजली चोरी के आरोप में बुरे फंसे सांसद जिया उर रहमान, अब 19100000 का भरना पड़ेगा जुर्माना\n\nJaipur: जयपुर में पेट्रोल पंप पर बड़ा ब्लास्ट, 5 लोगों की मौत, 35 गंभीर घायल, 30 वाहन जले\n\nUP: कन्नौज में लाखों खर्च कर करवाया जेंडर चेंज, फिर रचाई शादी, जानें पूरा मामला\n\nभारत को आंखे दिखा रहे Bangladesh की पाकिस्तान संग पक रही खिचड़ी? काहिरा में मिले शहबाज और मोहम्मद यूनुस\n\nPushpa 2: 1500 करोड़ के क्लब में शामिल हुई अल्लू अर्जुन की फिल्म, फिर भी रह गई इस मूवी से पीछे\n\nNoida: स्कूल वॉशरूम के बल्ब होल्डर में मिला कैमरा, मोबाइल पर लाइव देखता पकड़ा गया डायरेक्टर\n\nSushant Singh Rajput की बहन ने लुटाया Ankita Lokhande पर प्यार, एक्ट्रेस के बर्थडे पर कही ये बात\n\nबढ़ा हुआ पेट बना युवक के लिए आफत, सीढ़ियों में फंसने का Video Viral\n\nReliance Jio ने किया JioTag Go डिवाइस को लॉन्च, अब एंड्रॉइड डिवाइस खोने का डर खत्म\n\nRussia Ukraine War: यूक्रेन ने मार गिराए उत्तर कोरिया के 100 सैनिक, अब क्या एक्शन लेंगे किम जोंग उन?\n\nअभिषेक-ऐश्वर्या के बीच है सब ठीक, तलाक की अफवाहों के बीच बच्चन परिवार संग दिखीं एक्ट्रेस\n\nबाहर कड़ाके की सर्दी फिर भी अंदर से गर्म रहेगा घर, बिना हीटर होगा काम, फॉलो करें ये 5 टिप्स\n\nWeather Update:अब शीतलहर बढ़ाएगी दिल्ली वालों की मुसीबत, यूपी-बिहार में तेजी से गिरने लगा पारा, जानिए आज के मौसम का हाल\n\nViral: दूसरी शादी का प्लान है क्या? पति के हेलमेट नहीं पहनने पर IPS ने ऐसे सिखाया सबक, देखें Video\n\nबुढ़ापे को दूर और आपको जवां रखेंगी ये 5 आदतें, जरूर फॉलो करें ये Anti Aging Habits\n\nसंभल: सपा सांसद जियाउर रहमान बर्क के खिलाफ FIR, 1 करोड़ 91 लाख का लगा जुर्माना, जानें क्या है मामला\n\nBihar Viral News: तीन बच्चों की मां और दो बच्चों के बाप के अजब प्यार की गजब कहानी, जानकर हैरान रह जाएंगे\n\nधक्का-मुक्की मामले में राहुल गांधी के खिलाफ FIR दर्ज, BNS की इन धाराओं में हुआ केस, जानें कितनी है सजा\n\nRashifal 20 December 2024: कन्या और वृश्चिक वालों को होगा धन लाभ, जानें आज मेष से मीन तक की राशियों का भाग्यफल\n\nSDM की गाड़ी का व्हील लॉक करना 6 कर्मचारियों को पड़ा भारी, दिनभर थाने में रखा बंद\n\nUS से सामने आया Bird Flu का पहला Severe Human Case, क्या महामारी बन सकती है ये बीमारी?\n\n50 पुरुष, 10 साल: कौन है Dominique Pelicot? जिसे अपनी बीवी के Mass Rape के लिए हुई 20 साल की सजा?\n\nसर्दियों में इस ड्राई फ्रूट को खाने से दूर रहेंगी बीमारियां, जानिए फायदे और कैसे करें इस्तेंमाल\n\nरोमियो पकड़ रही महिला पुलिस से ही कर दी छेड़छाड़, योगीराज में भी Moradabad में मनचलों के हौसले बुलंद\n\nमांसपेशियों, Immunity को रखना है मजबूत? ठंड में खाना शुरू कर दें ये 10 फल\n\nPunjab Terror Attack: पंजाब में 25 दिन में सातवां आतंकी हमला, पुलिस चौकी पर फेंका ग्रेनेड, पढ़ें अपडेट्स\n\nधक्कामुक्की मामले में राहुल गांधी के खिलाफ शिकायत, BJP सांसद का आरोप- मेरे साथ कुछ ऐसा हुआ...\n\nWinter Health: ठंड में खूब पी रहे हैं गुनगुना पानी? ये लोग करें अवॉइड, फायदे के बजाए पहुंचा सकता है नुकसान\n\n'वो लंपट छिछोरा...' Ranbir Kapoor को राम बनना 'शक्तिमान' को नहीं आ रहा रास! कह बैठे विवादित बात\n\nFarmer Protest: 'बुजुर्ग किसान भूखा है और आप सब सही बता रहे' किसान नेता डल्लेवाल की तबीयत बिगड़ने पर भड़का सुप्रीम कोर्ट, पढ़ें पूरी बात\n\nVirat Kohli का बच्चों की वजह से मेलबर्न एयरपोर्ट पर हुआ पत्रकार से झगड़ा, जानें पूरा विवाद\n\nसुनीता विलियम्स की धरती पर वापसी मार्च 2025 तक टली, आखिर क्यों मजबूर हुई NASA?\n\n'अंबेडकर के मुद्दे पर ध्यान भटकाना चाहती है BJP', धक्कामुक्की कांड पर बोले राहुल गांधी\n\nAtul Subhash Case: कहां है अतुल सुभाष का 4 साल का बेटा? पत्नी निकिता ने अब खुद बताई सच्चाई\n\nKulgam Encounter: आतंकी संगठन या कॉरपोरेट कंपनी? एनकाउंटर में ढेर 5 आतंकियों से मिले ID कार्ड, 5 पॉइंट्स में पढ़ें पूरी बात\n\nठंड में बढ़े हुए यूरिक एसिड को काबू में रखेंगी ये चीजें, आज ही डाइट में करें शामिल\n\nकौन हैं '12th फेल' IPS मनोज शर्मा की वाइफ? डॉक्टरी की पढ़ाई के बाद UPSC क्रैक कर बनीं IRS\n\nआखिरकार 'राजा बाबू' का बेटा 2025 में करेगा धांसू डेब्यू, पापा से भी कहीं ज्यादा है हैंडसम\n\nShocking News: सरकारी हॉस्टल में चूहे ने 8 बार काटा, लड़की को मार गया लकवा, हैरान कर देगी ये घटना\n\n'परीक्षा पे चर्चा' में हिस्सा लेकर PM मोदी से सवाल पूछने का मौका, CBSE ने बताया कैसे करें आवेदन\n\nRussia-Ukraine War: थोड़ा वक्त लगा, लेकिन यूक्रेनी राष्ट्रपति ने रूस-युद्ध को लेकर सच बोल ही दिया!\n\n15 साल पहले ही इस Pakistani हसीना को ऑफर हुई थी Heeramandi, काम ना करने का अब भी है अफसोस\n\nसंतरे ही नहीं इसके छिलके भी सेहत के लिए होते हैं बेहद फायदेमंद, भूलकर भी न करें फेंकेने की गलती\n\nUP: मेरठ में सिर पर बाल उगाने की दवा बेचने वाले हुए गिरफ्तार, सैकड़ों लोग हुए थे एलर्जी के शिकार\n\nRSS: 'पहले भारत को अल्पसंख्यकों पर मिलती थी सलाह, दूसरे देशों में जो हो रहा है हम देख रहे हैं', मोहन भागवत का बड़ा बयान\n\nइस शख्स का स्टाइल है अलग! ई-रिक्शा लोडर के अनोखे अंदाज को देख लोग रह गए दंग, देखें Viral Video\n\nसिर से झड़कर गिरने लगता है डैंड्रफ तो इन चीजों को कपूर में मिलाकर लगाएं\n\nVastu Tips: वास्तुदोष से हैं परेशान तो घर में लगा लें ये 5 पेंटिंग्स, दूर हो जाएगी नकारात्मकता\n\nGujarat News: 7 महीने की प्रेग्नेंट पत्नी को पति ने बताया लेस्बियन, HC में लगाई ढूंढ़कर घर लाने की अर्जी\n\nक्या है Marburg Virus? जिसमें आंख-नाक से आने लगता है खून, खराब हो जाते हैं शरीर के ये अंग\n\nकोसा सिल्क साड़ी की बढ़ती डिमांड, जानिए कैसे कोकून से बनती हैं खूबसूरत साड़ियां",
            "source": {
                "uri": "dnaindia.com",
                "dataType": "news",
                "title": "Daily News and Analysis (DNA) India"
            },
            "authors": [
                {
                    "uri": "मीना_परजापति@dnaindia.com",
                    "name": "मीना प्रजापति",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://cdn.dnaindia.com/sites/default/files/2024/12/20/7143730-sanjay-26.jpg",
            "eventUri": None,
            "sentiment": None,
            "wgt": 37,
            "relevance": 1
        },
        {
            "uri": "8429353199",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "09:02:11",
            "dateTime": "2024-11-26T09:02:11Z",
            "dateTimePub": "2024-11-26T09:01:41Z",
            "dataType": "news",
            "sim": 0.5137255191802979,
            "url": "https://www.firstpost.com/opinion/26-11-the-day-india-changed-forever-13838964.html",
            "title": "26/11: The day India changed forever",
            "body": "A policeman pushes a barricade to be erected in front of the Taj Mahal Hotel in Mumbai. The iconic hotel was one of the many spots that the 10 terrorists targeted on the night of November 26, 2008, which is now remembered as the 26/11 attacks. File image/Reuters\n\nThere are points in a nation's history that become watershed moments from where the trajectory of a nation takes an irreversible turn. In the history of independent India too, there have quite a few such path-breaking events. If the first war between India and Pakistan triggered by an infiltration by tribal militias 'Kabalias' in October 1947 hastened the amalgamation of Kashmir into the Indian Union, the 1971 war led to the birth of a new nation, Bangladesh, and the 1999 Kargil War led to a complete review of border security and intelligence infrastructure along the northern Kashmir.\n\nHowever, if there was one event that shook India and has transformed the Indian security mindset, it has to be the Mumbai terror attack of November 26, 2008. It was not as if this was the first terror attack outside Jammu & Kashmir because the Parliament attack of December 2001 or the Pune German Bakery Blast of February 2010 were significant too. But the manner in which India fought back and the fact that the 26/11 attacks specifically targeted places frequented by foreigners, especially Jews, made it even more significant in terms of a security landmark.\n\nWhat Happened That Day?\n\nThe night of November 26, 2008, 10 terrorists from the Lashkar-e-Taiba (LeT) terror group of Pakistan entered Mumbai city across the sea route in inflatable speedboats after embarking from Karachi in a trawler on November 21. Having entered Mumbai fairly undetected and uncontested, they split into small teams to carry out coordinated attacks in carefully chosen places to cause maximum impact. Over the course of the next four days, they killed 166 people and injured 300. The targets -- the Taj and Oberoi Hotels, Chhatrapati Shivaji Maharaj Railway Terminus, the Jewish Centre at Nariman House, and the Leopold Cafe -- were carefully chosen, surveyed in detail, and targeted specifically, since these places were often frequented by foreigners, especially Europeans and Jews.\n\nAmong the 166 killed were 141 Indians and 25 foreign nationals, including 6 Americans and 4 Israelis. According to transcripts of phone calls between the terrorists and their handlers during the attack, terrorists were specifically instructed to kill foreigners, especially Jews. Nine terrorists were eliminated while Ajmal Kasab was captured alive, who later confessed to the conspiracy being hatched in Pakistan and executed by LeT.\n\nWhat Changed Thereafter\n\n26/11 was not the biggest terror attack in India and not the last too. The 1993 Mumbai serial attacks had killed 257 people, while the 2006 Mumbai train attack had killed 209 people. 14 months later, the Pune German Bakery Blast in February 2010 too resulted in 18 deaths, including 5 foreign nationals. However, what perhaps changed after 26/11 was the way it shook the national security consciousness. Having witnessed the visuals live on television over four days, it became embedded in public memory forever too.\n\nThere were two other major structural changes that took place, among many others. Firstly, a specific focus was now put on coastal security, with the Indian Navy being entrusted with the overall responsibility of maritime security, including coastal security and offshore security, while the Coast Guard was to guard the territorial waters. The National Command Control Communications and Intelligence (NC3I) Network was set up as part of the maritime security measures.\n\nSurveillance across the long coastline was a challenge. Coupled with satellite coverage, many other measures were instituted, including the fact that all boats with a length greater than 20 meters were required to have an Automatic Identification System (AIS). Systems for better coordination between local police and other security and intelligence agencies too were put in place with the National Investigation Agency (NIA) being set up in December 2008. The National Security Guard (NSG), which operated from Delhi earlier, now had new bases across the country for faster response.\n\nHowever, the biggest change for India that happened as a result of the attack was that for the first time since the 1990s, when India's fought against terror took shape, there was a near unanimous global acceptance that India was fighting its 'war against terror'. Earlier, despite volumes of evidence of Pakistan-based terror attacks in India, most countries and global platforms were rather dismissive about Indian claims, leaving India to fight its battle alone.\n\nThe 26/11 also led to greater intelligence sharing mechanisms between the countries, especially the US, EU, Israel, and Russia, as well as the West Asian region. The acceptance of the Indian line on terror had another significant outcome, something that the Modi government fully capitalised on after 2014, which led to vastly enhanced relations with countries in West Asia and built a number of strategic partnerships.\n\nAgainst a compulsive show of Muslim solidarity with Pakistan earlier, thereby limiting the options to enhance ties with India, there was now a unanimous acceptance of India's position on terror, and on more than one occasion thereafter, the countries in the region have strongly supported India. Whether it was Uri, Pathankote, or Pulwama, countries in the region, especially Saudi Arabia, the UAE, Bahrain, and Qatar, not only condemned the attacks strongly but extended support to India in any action (including military) that it took to fight and eradicate terror.\n\nThe Pakistan Factor\n\nA significant result of 26/11 has been India's stance towards Pakistan and its 'no talks till no terror' policy and Noneifying the 'Pakistan Factor' in all forums in all possible ways. It has not only led to the isolation of Pakistan in the region but has starved it economically too. The proofs of financial support by Pakistan to terror submitted by India and other global agencies have led to the Financial Action Task Force (FATF), a global body that investigates and grades nations on issues of combat money laundering and terrorist financing, sanctioning Pakistan multiple times in the past decade and placing severe restrictions on international aid into the country.\n\nIn addition, Pakistan, which was the poster boy of US policy and the fight against terror in Afghanistan in 2008-09, now finds itself completely out of favour. To add to its woes, with the US-led international forces having left Afghanistan in August 2021, Pakistan is not only left high and dry from a financial point of view but has to also contend with terror attacks on its own soil frequently. Plus, due to India's success in de-hyphenating its ties from the Pakistan factor with the countries in West Asia, the blanket support and aid that Pakistan got from the region earlier is no longer forthcoming.\n\nPerhaps the biggest change has been in the policy mindset of the Indian security establishment. Whether it was Uri in 2016, Pathankot in 2016, or Pulwama in 2019, India, through prompt and effective surgical strikes, has made it clear that Pakistan cannot get away with terror attacks any longer. Also, the nuclear bogey of Pakistan too has been called out, with the air strike deep into Pakistan in Balakot being a clear example of it.\n\nConclusion\n\n26/11, often called the 9/11 of India, was a dark chapter in India's security history, an event that shook the collective security consciousness of India and changed the security paradigm in the region forever. It also made India realise that terror cannot be 'taken in the stride' any longer and that any future attack has to be replied with strong punitive measures in a 'whole of nation approach'.\n\nThe changed approach in Kashmir, with a focus on two-pronged strategy: focus on economic development and infrastructure development on the one hand and very close coordination between the security agencies on the other, has resulted in a drastic reduction in terror threats manifesting within India over the years. The abrogation of Article 370 from Kashmir in August 2019 too has contributed to ensuring closer integration of the region with India. Who knows how much and how soon these changes would have happened if 26/11 had not forced us to wake up?",
            "source": {
                "uri": "firstpost.com",
                "dataType": "news",
                "title": "Firstpost"
            },
            "authors": [],
            "image": "https://images.firstpost.com/uploads/2024/11/mum1-2024-11-844d98397fdb0189c02e341ea7c40fcf.jpg?im=FitAndFill=(1200,675)",
            "eventUri": "eng-10118850",
            "sentiment": -0.403921568627451,
            "wgt": 37,
            "relevance": 34
        },
        {
            "uri": "8452898605",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-11",
            "time": "14:49:15",
            "dateTime": "2024-12-11T14:49:15Z",
            "dateTimePub": "2024-12-11T14:48:59Z",
            "dataType": "news",
            "sim": 0.7176470756530762,
            "url": "https://www.outkick.com/sports/floyd-mayweather-attacked-pro-palestinian-mob-supporting-israel",
            "title": "Floyd Mayweather Attacked By Pro-Palestinian Mob For Supporting Israel",
            "body": "Floyd Mayweather was attacked and chased by a group of angry pro-Palestinian supporters earlier this week and the whole thing was caught on video.\n\nThe legendary boxer had been shopping in London's Hatton Garden's area when he was approached inside by a couple of men who asked about his support for Israel. When Mayweather double-downed and responded that he was, \"Proud to support the Jews,\" the Palestinian mob soon became aggressive and all hell broke loose.\n\nVideo shows Mayweather getting rushed out of the store and into the street as he and his bodyguards, who are clearly outnumbered, try to get to their vehicles and get the 47-year-old away from the threat. At one point, someone tried to take a couple of swings at Floyd but fortunately for the pro-terror supporter, he didn't connect, because their face probably would never have been the same if Mayweather got hold of him.\n\nThroughout the whole ordeal, you hear Mayweather being called racial slurs and anti-Israeli statements are being shouted.\n\nFloyd Mayweather has been one of the most vocal supporters of Israel, especially since the October 7th terror attack. Earlier this summer, Floyd even took his private jet and flew supplies to Tel Aviv.\n\nMeanwhile, London continues to be a hotbed of antisemitism. The BBC reports that there were nearly 2,000 anti-Jewish hate crimes in the United Kingdom from January to June of this year, with more than half occurring in London. The numbers were based on figures from a Jewish security charity.\n\nAll one has to do is check social media to see the mindset of some of the people that Floyd was up against and also to see their coward mentality.",
            "source": {
                "uri": "outkick.com",
                "dataType": "news",
                "title": "OutKick"
            },
            "authors": [
                {
                    "uri": "mike_gunzelman@outkick.com",
                    "name": "Mike Gunzelman",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://static.outkick.com/www.outkick.com/content/uploads/2024/12/floyd-mayweather-israel.jpg",
            "eventUri": "eng-10161415",
            "sentiment": -0.1294117647058823,
            "wgt": 36,
            "relevance": 1
        },
        {
            "uri": "8467263569",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-20",
            "time": "21:33:27",
            "dateTime": "2024-12-20T21:33:27Z",
            "dateTimePub": "2024-12-20T21:33:04Z",
            "dataType": "news",
            "sim": 0.4274509847164154,
            "url": "https://tribuneonlineng.com/one-dead-about-70-injured-as-car-crashes-into-german-christmas-market/",
            "title": "One dead, about 70 injured as car crashes into German Christmas market",
            "body": "A car rammed into a crowded Christmas market in Magdeburg, Germany, on Friday, leaving one person dead and nearly 70 others injured in what authorities suspect to be a terror attack.\n\nAccording to the UK Telegraph, the attack occurred at 7.04 pm local time in Magdeburg, the provincial capital of Saxony-Anhalt, located west of Berlin, with a population of about 240,000.\n\nEyewitnesses recounted how the vehicle smashed through barriers designed to protect the market, driving directly into unsuspecting shoppers.\n\nVideo footage from a nearby camera reportedly captured the car speeding through a narrow alleyway lined with stalls, mowing down pedestrians in its path.\n\nALSO READ: UK: DWP announces Christmas, New Year payment dates for Universal Credit, PIP, others\n\nAccording to Germany's DPA news agency, the driver of the dark-coloured BMW has been arrested, while police have cordoned off the city centre, searching for potential explosives linked to the incident.\n\nThe Chancellor of Germany, Olaf Scholz, expressed his shock, stating, \"My thoughts are with the victims and their loved ones.\"\n\nAuthorities have maintained a strong security presence around the suspect's car, which remains at the scene. German public broadcaster MDR reported that an explosive device might be inside the vehicle.\n\nReacting to the development on X, Tesla owner Elon Musk called for the resignation of Chancellor Scholz.\n\nHe tweeted, \"Scholz should resign immediately. Incompetent fool.\"",
            "source": {
                "uri": "tribuneonlineng.com",
                "dataType": "news",
                "title": "Tribune Online"
            },
            "authors": [
                {
                    "uri": "adam_mosadioluwa@tribuneonlineng.com",
                    "name": "Adam Mosadioluwa",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://tribuneonlineng.com/wp-content/uploads/2024/12/German-Police-1.jpeg",
            "eventUri": "eng-10192203",
            "sentiment": -0.1137254901960785,
            "wgt": 35,
            "relevance": 1
        },
        {
            "uri": "2024-12-578054772",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-17",
            "time": "06:57:41",
            "dateTime": "2024-12-17T06:57:41Z",
            "dateTimePub": "2024-12-17T06:54:34Z",
            "dataType": "news",
            "sim": 0.4627451002597809,
            "url": "https://www.abc.net.au/news/2024-12-17/victorian-protest-laws-reforms-explained/104736396",
            "title": "Victoria will reform its laws around protesting. Here's what's changing",
            "body": "The Victorian government has announced plans to increase police powers around protests in a bid to curb anti-Semitism and other forms of extremism.\n\nIt follows a suspected terror attack on a Melbourne synagogue, with the government now moving to protect religious worship in the state.\n\nAs part of the measures, police will be given greater powers when dealing with protesters, including an increased ability to search for certain items and enforce a total ban on face coverings.\n\nThe proposed legislation is yet to be finalised and must pass through parliament before becoming law.\n\nThe government will implement a mask ban at public demonstrations in Victoria.\n\nCurrently, if a protester refuses to remove their face mask, Victorian police can only ask the protester to leave the area.\n\nPolice must reasonably believe that the person is wearing the face covering primarily to conceal their identity or to protect themselves from the effects of crowd-controlling substances.\n\nThe proposed laws would give police the power to force a protester to remove their face mask or face arrest.\n\nMinister for Police Anthony Carbines said face coverings were increasingly used by people who wished to hide their identity while committing violence.\n\n\"If they're not removed, you can be arrested and charged.\"\n\nMr Carbines said exemptions would be made for legitimate health, religious or cultural reasons.\n\nPolice will also be granted greater powers to seize \"attachment devices\" -- things such as glue, rope, chains and locks used by protesters to secure themselves to the site of a protest.\n\nA number of incidents involving protesters gluing or attaching themselves to public spaces made headlines in 2024, including a climate protest atop a truck on the West Gate Bridge.\n\nIn September, a protester was arrested and charged after using concrete to secure herself to the boot of a car in the middle of a protest.\n\nUnder the proposed laws, police will be given the power to stop and search people or their vehicles if they suspect they have a dangerous attachment device, and then seize any found devices.\n\nMr Carbines said under the current law, police had to return such attachment devices to \"offenders\" if they were found.\n\n\"We know that attachment devices that people use put first responders at risk, in both removing offenders and making a situation safe, they disrupt the economy, they disrupt people from going about their lawful activities,\" he said.\n\nThe government will also move to establish \"safe access areas\" around places of religious worship such as churches, temples, mosques and synagogues.\n\nIt comes after recent protests outside synagogues in both Sydney and Melbourne.\n\nThe size of the safe zones around religious buildings is yet to be determined, with the government saying it will consult with religious leaders and communities on the matter.\n\nThe Victorian government previously established protest-free zones for the forestry industry in 2022, creating \"Timber Harvesting Safety Zones\" on worksites where any protest activity is penalised.\n\nFinally, state laws will be introduced to ban the flags and symbols of listed terrorist organisations, which the government says will fill gaps in Commonwealth anti-terror legislation.\n\nWhat is the legal community's reaction?\n\nBarrister Michael Stanton, the previous president of civil liberties organisation Liberty Victoria, said the announcement appeared to be a \"kneejerk response\".\n\nMr Stanton said the government had wrongly conflated the recent criminal act at the Adass Israel Synagogue in Ripponlea with peaceful protesting.\n\n\"There is simply no link between that and the protest movement that's been occurring for well over a year now,\" he said.\n\n\"To use that really shocking event to try to clamp down on the right to protest is deeply concerning.\"\n\nMr Stanton said the nature of protests in Melbourne's CBD, which brought them in close proximity to places such as St Paul's Cathedral, would make the government's legislation \"unworkable\".\n\n\"Banning protest outside of places of worship as a blanket rule can't be reasonable, it can't be proportionate,\" he said.\n\nDavid Mejia-Canales, a senior lawyer at the Human Rights Law Centre, said the government's plans currently lacked detail and required more scrutiny.\n\n\"There are some very real concerns in what has been announced by the premier,\" he said.\n\n\"There are a lot of measures the premier has announced that are going to give the police wideranging and discretionary powers to target and to search anyone attending protests. This will only lead to police abuses against peaceful protesters.\"\n\nMr Mejia-Canales said the government needed to ensure any limitations on people's ability to gather peacefully needed to be \"lawful, necessary and proportionate to what they're trying to fix\".\n\n\"And we need to actually make sure that those limitations are precise and that they balance everyone's rights properly,\" he said.\n\n\"I would caution the government that rushed and kneejerk lawmaking will not make anyone safer whatsoever.\n\n\"This needs a careful, considered and consultative approach.\"\n\nWhat is the reaction from stakeholders?\n\nConvenor of protest group Students for Palestine Jasmine Duff said the proposed law reforms were an attack on the rights of protesters.\n\n\"I think it's absolutely appalling that the Victorian government is trying to limit our democratic rights to protest, to crack down on civil liberties right in the middle of a very deeply important anti-war movement,\" Ms Duff said.\n\n\"We're going to keep coming out, we're going to keep demonstrating no matter what laws are introduced by the government.\"\n\nShe said attachment devices such as glue and locks were uncommon at pro-Palestinian protests and described the ban as a political tactic.\n\nIn contrast, Anti-Defamation Commission chairman Dvir Abramovich called the reforms a \"game changer\" that would help protect the Victorian Jewish community.\n\n\"We've asked for action and the government has delivered a hammer blow to those thugs who think they can turn synagogues into war zones,\" he said.\n\n\"It's sent a message to those hiding behind masks, your days of hiding are over.\"",
            "source": {
                "uri": "abc.net.au",
                "dataType": "news",
                "title": "Australian Broadcasting Corporation"
            },
            "authors": [],
            "image": "https://live-production.wcms.abc-cdn.net.au/2cd156efb00442339e8058a8358599a4?impolicy=wcms_watermark_news&cropH=2813&cropW=5000&xPos=0&yPos=260&width=862&height=485&imformat=generic",
            "eventUri": "eng-10179298",
            "sentiment": -0.05882352941176472,
            "wgt": 35,
            "relevance": 1
        },
        {
            "uri": "2024-11-560758574",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-29",
            "time": "10:51:34",
            "dateTime": "2024-11-29T10:51:34Z",
            "dateTimePub": "2024-11-29T10:51:27Z",
            "dataType": "news",
            "sim": 0.7882353067398071,
            "url": "https://m.jpost.com/breaking-news/article-831321",
            "title": "Several wounded after terrorist opens fire in West Bank",
            "body": "Four people were wounded in a shooting at a bus near Ariel in the West Bank, Magen David Adom (MDA) announced on Friday.\n\nMDA paramedics were transferring to the Rabin Medical Center-Beilinson Campus in Petah Tikva three people in serious condition and one in moderate condition.\n\nMDA added that four additional individuals had sustained light wounds from glass shards.\n\nTerrorist apprehended\n\nThe IDF said it had received reports of a terror attack and that the terrorist had been thwarted. Advertisement\n\nThis is a developing story.",
            "source": {
                "uri": "m.jpost.com",
                "dataType": "news",
                "title": "The Jerusalem Post | JPost.com"
            },
            "authors": [],
            "image": "https://images.jpost.com/image/upload/q_auto/f_auto,fl_lossy/c_fill,g_faces:center,h_407,w_690/636700",
            "eventUri": "eng-10129334",
            "sentiment": -0.3254901960784313,
            "wgt": 34,
            "relevance": 1
        },
        {
            "uri": "8463702056",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-18",
            "time": "17:10:45",
            "dateTime": "2024-12-18T17:10:45Z",
            "dateTimePub": "2024-12-18T17:10:27Z",
            "dataType": "news",
            "sim": 0.7529411911964417,
            "url": "https://www.tribuneindia.com/news/j-k/shifting-yasin-maliks-terror-trial-from-jammu-to-delhi-sc-asks-co-accused-to-respond-to-cbis-plea/",
            "title": "Shifting Yasin Maliks terror trial from Jammu to Delhi: SC asks co-accused to respond to CBIs plea - The Tribune",
            "body": "As the CBI seeks transfer of trial in a case against Kashmiri separatist leader and JKLF chief Yasin Malik in connection with two cases, including the murder of 4 Indian Air Force (IAF) personnel in 1989, the Supreme Court on Wednesday asked six co-accused to respond to the agency's plea.\n\nAsking the co-accused to file their replies in two weeks, a Bench led by Justice Abhay S Oka posted the matter for further hearing on January 20, 2025.\n\nThe direction came after the Bench was told that one of the 10 accused has died while others have not filed their replies. \"All the accused have to be heard if the trial is to be transferred,\" Justice Oka said.\n\nThe CBI has challenged a Jammu court's order for the physical production of Malik to face trial in the case. Currently lodged in Tihar Jail in Delhi, Malik insisted on being physically present in Jammu to cross-examine witnesses.\n\nThe Jammu Special Court has sought Malik's appearance for cross-examination of witnesses in two cases - the killing of four IAF personnel and abduction of Rubaiya Sayeed, daughter of late Mufti Muhammad Sayeed -- a former Chief Minister of erstwhile state of Jammu and Kashmir -- in 1989.\n\nThe top court had issued notice on the CBI's petition in April 2023 and stayed the Jammu court's order.\n\nNoting that even 26/11 Mumbai terror attack case accused Ajmal Kasab was given fair trial in India, the Bench had on November 21 suggested setting up a court in jail to cross-examine Malik.\n\nDescribing him as \"just not another terrorist\", Solicitor General Tushar Mehta had last month said, \"We do not want to take him to Jammu and Kashmir because of the offence in which he has been convicted...The Government cannot go by the book in such cases.\"\n\nMalik was physically present in the Supreme Court during a hearing in July 2023 after intimating jail authorities that he wanted to physically attend the hearing. Mehta had then written a strongly-worded letter to the Home Secretary highlighting that Malik's presence in the Supreme Court was a grave security lapse.",
            "source": {
                "uri": "tribuneindia.com",
                "dataType": "news",
                "title": "Tribuneindia News Service"
            },
            "authors": [],
            "image": "https://www.tribuneindia.com/sortd-service/imaginary/v22-01/jpg/large/high?url=dGhldHJpYnVuZS1zb3J0ZC1wcm8tcHJvZC1zb3J0ZC9tZWRpYTM0YjEwMDYwLWJkNjAtMTFlZi05OTIxLWJmNzYyZWY2NmVmNS5qcGc=",
            "eventUri": "eng-10183467",
            "sentiment": -0.1529411764705882,
            "wgt": 34,
            "relevance": 1
        },
        {
            "uri": "2024-12-575471043",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-14",
            "time": "02:21:20",
            "dateTime": "2024-12-14T02:21:20Z",
            "dateTimePub": "2024-12-14T02:20:50Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.timesofisrael.com/liveblog_entry/idf-airstrike-targeted-terror-operatives-who-were-heading-to-attack-troops-in-gaza/",
            "title": "IDF: Airstrike targeted terror operatives who were heading to attack troops in Gaza",
            "body": "The military releases an overnight statement saying an Israeli aircraft struck a cell of operatives in Gaza while \"on their way to carry out terror [attack] plans against our forces in the Strip and toward Israeli territory in the immediate future.\"\n\nAn IDF statement says the targeted operatives were at a school in Gaza City when struck, adding that \"many measures were taken to reduce the chance of harm\" to non-combatants.\n\nThe statement also accuses Palestinian terror groups of violating international law by operating in civilian facilities and using civilian shields, without specifying which factions the targeted operatives belonged to.",
            "source": {
                "uri": "timesofisrael.com",
                "dataType": "news",
                "title": "timesofisrael.com"
            },
            "authors": [],
            "image": "https://static.timesofisrael.com/www/images/toi-ln-1200.png",
            "eventUri": None,
            "sentiment": -0.7019607843137254,
            "wgt": 33,
            "relevance": 1
        },
        {
            "uri": "8442232871",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-04",
            "time": "15:10:09",
            "dateTime": "2024-12-04T15:10:09Z",
            "dateTimePub": "2024-12-04T15:09:57Z",
            "dataType": "news",
            "sim": 0.3411764800548553,
            "url": "https://nypost.com/2024/12/04/us-news/train-hero-alek-skarlatos-on-daniel-penny-trial-this-could-happen-to-you/",
            "title": "Train hero who helped stop 2015 terror attack gives warning over...",
            "body": "Michael Ruiz, Ashley Papa and Stephen Sorace and The Associated Press, Fox News\n\nThe Oregon Army National Guard veteran who helped thwart a terror attack on a train from Amsterdam to Paris in 2015 is warning that New York Marine veteran Daniel Penny's manslaughter trial is concerning to all those who think of themselves as \"someone who would step up.\"\n\nOregon House Rep.-elect Alek Skarlatos, who along with two friends and another good Samaritan disarmed and subdued the Moroccan terrorist Ayoub El Khazzani when he opened fire on a packed Thalys train, said he believes French self-defense law is more accommodating than in the Empire State.\n\n\"Do you want people to step up and try to do the right thing or not? I mean, if he, God forbid, is convicted, it's going to frighten a lot of people and blue states into inaction,\" he said.\n\nThe problem with blue states, he warned, is an apparent double standard where politicized prosecutors pick and choose winners and losers.\n\n\"I think if you live in Oregon, Washington, California, and New York, you are kind of concerned that something like this could happen to you, especially if you're someone who thinks of themself as someone who would step up,\" he told Fox News Digital. \"In our terrorist attack, for instance... it happened on a gun-free continent. I wasn't able to carry. We had to fight this guy by hand.\"\n\nSkarlatos sees a two-tiered justice system in Democratic strongholds. Penny remained at the scene, spoke with police, and was not arrested until 11 days later when the same Manhattan District Attorney's Office that prosecuted the controversial NY v. Trump case indicted Penny on manslaughter charges.\n\n\"Hunter Biden is being pardoned today as well,\" Skarlatos said. \"There's all sorts of double standards when it comes to how blue states and Democrat leadership enforce the law.\"\n\nHe also said he believes Penny acted with others in mind, stepping in to stop an apparent threat before it got out of hand.\n\n\"If you watched his interview with police after the fact, he thought that he did the right thing and the police had Neely in custody and everything was going to be fine,\" he said.\n\nSkarlatos and two childhood friends, Spencer Stone and Anthony Sadler were on board a Paris-bound train on Aug. 21, 2015, when El Khazzani jumped out of the bathroom and opened fire.\n\nThe now-convicted terrorist had an AK-47 rifle, an automatic pistol, a box cutter, and hundreds of rounds of ammunition.\n\nThe rifle jammed and they wrestled the guns away. By then, El Khazzani had shot one passenger, seriously slashed Mark Moogalian, an American ex-pat who was living in France and was first to engage the gunman and cut Stone multiple times.\n\n\"When we kind of got control of him and had him bent over kind of a table in the train car, he was still fighting to get away, and so I just told him, 'Stop resisting, stop resisting.' And he didn't. So I put the handgun to the back of his head and pulled the trigger. And the handgun turned out to be completely empty,\" he said.\n\nSkarlatos cracked him in the head with the butt of the rifle instead, as Stone, who nearly lost his thumb, choked him out.\n\nThe former Oregon National Guard sniper said he was afraid to tell French authorities at first.\n\n\"I actually asked the American FBI, who interviewed us the next morning, if it was something that the French would have a problem with,\" he said. \"And they said, no, pretty much it's terrorism. They don't care. You can do whatever you want to terrorists in France. And so, when the French federal police interviewed me later that same day, I told them about that.\"\n\nThe three childhood friends received the French Legion of Honor, France's highest award, in 2015. Skarlatos was also given the Army's Soldier's Medal in a ceremony at the Pentagon.\n\nStone, who said later his medical training helped save the life of the fourth passenger who stepped in, Moogalian, received the Airman's Medal and Purple Heart.\n\nAll three were invited to the White House when they returned home.\n\nThey later played themselves in the Clint Eastwood-directed movie based on their memoir, \"The 15:17 to Paris\" in 2018.\n\nPenny's case has received national attention since the 26-year-old veteran's arrest on manslaughter and criminally negligent homicide charges in May 2023.\n\nHe placed Jordan Neely, a 30-year-old homeless man with schizophrenia and synthetic marijuana in his system, in a headlock to stop a fear-inducing outburst on a Manhattan subway car.\n\nNeely had an active arrest warrant at the time, and a history of violent attacks, and witnesses testified that they feared for their lives as Neely screamed about killing people and not being afraid to go back to jail.\n\nPenny's defense has argued that the restraint was a justified use of force and that it was not the sole factor in Neely's death. Prosecutors accuse Penny of taking the move too far.\n\nHe faces a maximum of 15 years in prison if convicted.\n\nSkarlatos was elected to the Oregon House of Representatives last month.\n\nOnce he takes office, he said, he hopes to oppose restrictive gun control measures and ensure citizens have a chance to defend themselves.\n\n\"Word on the street is the Democrats are going to be bringing a lot of anti-gun bills, which is kind of my pet cause, so to speak, being a gun owner and surviving what we survived in France,\" he said.",
            "source": {
                "uri": "nypost.com",
                "dataType": "news",
                "title": "New York Post"
            },
            "authors": [],
            "image": "https://nypost.com/wp-content/uploads/sites/2/2024/12/daniel-penny-leaves-courtroom-judge-94734849.jpg?quality=75&strip=all&w=1024",
            "eventUri": "eng-10141450",
            "sentiment": -0.2235294117647059,
            "wgt": 33,
            "relevance": 1
        },
        {
            "uri": "8466963433",
            "lang": "hin",
            "isDuplicate": False,
            "date": "2024-12-20",
            "time": "16:43:34",
            "dateTime": "2024-12-20T16:43:34Z",
            "dateTimePub": "2024-12-20T16:43:18Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.dnaindia.com/hindi/india/news-lok-sabha-lost-65-hours-during-winter-session-crime-branch-to-investigate-jostling-incident-in-parliament-4144353",
            "title": "शीतकालीन सत्र के दौरान लोकसभा में 65 घंटे का नुकसान, संसद में धक्का-मुक्का कांड की जांच करेगी क्राइम ब्रांच",
            "body": "UP Board: इस तारीख से होंगी यूपी बोर्ड इंटरमीडिएट की प्रैक्टिकल परीक्षाएं, जान लें पूरा शेड्यूल\n\nशीतकालीन सत्र के दौरान लोकसभा में 65 घंटे का नुकसान, संसद में धक्का-मुक्का कांड की जांच करेगी क्राइम ब्रांच\n\nCAG Report: भारतीय वायुसेना को नहीं मिल रहे पायलट, युद्ध हुआ तो...? जानें कैग रिपोर्ट में है किस बात की चिंता\n\nD Gukesh को सरकार ने दिया बड़ा तोहफा, प्राइज मनी पर नहीं देना होगा टैक्स, चेस चैंपियन बनने पर मिली थी इतनी राशि\n\n'जुबां संभालकर बोलो' Bangladesh-Pakistan के 'भाईचारे' के बीच भारत ने दी सीधी वॉर्निंग\n\nपवित्रा पुनिया का धर्म बदलवाना चाहते थे एजाज खान? खुद एक्टर ने बता दी ब्रेक-अप की पूरी सच्चाई\n\nगंदे कोलेस्ट्रॉल को खींच कर बाहर निकाल देंगे किचन में रखें ये मसाले, शरीर को मिलेंगे कमाल के फायदे\n\nYear ender 2024: वो 5 महिलाएं जिन्होंने वैश्विक स्तर पर बटोरीं सुर्खियां, हैं लोगों के लिए प्रेरणा\n\nRashifal 21 December 2024: तुला वालों को सताएगी चिंता, जानें आज मेष से मीन तक की राशियों का भाग्यफल\n\nअश्विन के बाद ये 4 खिलाड़ी भी जल्द ले सकते हैं इंटरनेशनल क्रिकेट से संन्यास! लिस्ट में दिग्गजों का नाम शामिल\n\nसर्दियों के सस्ते और ट्रेंडी कपड़े खरीदने हैं तो दिल्ली के इन 5 बाजारों में जरूर जाएं\n\nGoogle layoffs: गूगल में क्यों मच रहा हंगामा, सुंदर पिचई ने 10% स्टाफ के साथ क्या किया, समझें पूरा मामला\n\nU19 Womens Asia Cup 2024: भारत ने एशिया कप के सेमीफाइनल में दी श्रीलंका को मात, अब खिताब के लिए होगी बांग्लादेश से जंग\n\nNumerology 2025: साल 2025 में चमकेगी मूलांक 2 वालों की किस्मत, जानें करियर से लव लाइफ तक का हाल\n\nकौन थे ताशी नामग्याल, Indian Army ने क्यों दी एक चरवाहे के निधन पर उसे सलामी?\n\nAlia Bhatt से लेकर Deepika Padukone तक, 2024 में इन 6 बॉलीवुड हसीनाओं ने ग्लोबल मंच पर बढ़ाया देश का मान\n\nजवां दिखने के लिए अपनाएं ये घरेलु नुस्खे, बुढ़ापे की रफ्तार हो जाएगी धीमी\n\nअतुल सुभाष सुसाइड केस में क्या कहती है पुलिस की थ्योरी, बेमन शादी से लेकर आत्महत्या तक, कई खुलासे\n\nघर पहुंचा पार्सल, अंदर लाश देखकर उड़े होश, भेजने वाले ने मांगी 1.3 करोड़ की रंगदारी, पढ़ें पूरी बात\n\nDiabetes Management: इन 7 बातों का ध्यान रखें डायबिटीज के मरीज, कभी नहीं बढ़ेगा शुगर लेवल\n\nIND VS AUS BOXING DAY TEST: जानिए भारत का बॉक्सिंग डे टेस्ट में कैसा रहा है रिकॉर्ड? 26 दिसंबर को ऑस्ट्रेलिया से होगा सामना\n\nबांग्लादेश में हिंदुओं के खिलाफ हिंसा के 2,200 और पाकिस्तान में 112 मामले, सरकार ने जारी किए चौंकाने वाले आंकड़े\n\nUGC NET December 2024: यूजीसी नेट का टाइम टेबल जारी, जानें किस डेट को होगा किस सब्जेक्ट का एग्जाम\n\nसर्दियों में सेहतमंद रहने के लिए रोज खाएं ये फल, मौसमी बीमारियां रहेंगी कोसों दूर\n\nPalmistry: हथेली में इन 3 रेखाओं के मिलने से बनती है धन की कोठरी, जानें क्या मिलता है संकेत\n\nअडानी समूह की बड़ी सौगात, 20000 करोड़ का निवेश, अब यहां पावर प्लांट लगा देंगे 12000 नौकरियों के मौके\n\nDelhi News: भाजपा हेडक्वार्टर के बाहर मिला संदिग्ध बैग, इलाका सील, बम स्क्वॉयड बुलाया गया\n\nकितना बदल गया है TV का 'राम', तस्वीर शेयर करते ही हिला दिया पूरा इंटरनेट\n\nViral News: अश्विन ने रिटायरमेंट के बाद खोले बड़े राज, फोन का कॉल लॉग साझा कर कहा-मुझे दिल का दौरा पड़ जाता\n\nबहराइच में दिल्ली के कंझावाला जैसा केस, तहसीलदार की गाड़ी से टकराकर 30 किमी घिसटा युवक, उड़ गए चिथड़े\n\n'पंजाबी झुकेगा नहीं', Diljit Dosanjh ने अब महाराष्ट्र सरकार पर निकाली भड़ास, मुंबई कॉन्सर्ट से जुड़ा है मामला\n\nBhopal News: जंगल में खड़ी कार से निकला 52 किलो सोना, IT रेड करने वाली टीम भी खजाना देख दंग\n\nWinter Skin Care: सर्दियों में क्यों फटने लगती है स्किन? जानें कारण और बचाव के लिए घरेलू उपाय\n\nAtul Subhash Suicide: पत्नी निकिता ने अतुल सुभाष को बताया अय्याश, 'एक साथ 3 लड़कियों संग...'\n\nUP: मेरठ में भी हाथरस जैसी भगदड़, प्रदीप मिश्रा की कथा में बेकाबू हुई भीड़, कई बच्चे-महिलाएं कुचले\n\nSA Vs PAK ODI: पाकिस्तान ने वनडे सीरीज जीतने के लिए की चीटिंग? क्लासेन के दावे से सनसनी\n\nGaza में युद्ध विराम होगा या नहीं? Netanyahu ने अपना फैसला सुना दिया है!\n\nझुर्रियों को अब कहें अलविदा, इस पाउडर के इस्तेमाल से पाएं चांद जैसी चमकदार त्वचा\n\nOm Prakash Chautala Death: पढ़ने का ऐसा जज्बा कि तिहाड़ जेल से दिया एग्जाम, कितने एजुकेटेड थे ओमप्रकाश चौटाला?\n\nDigvijay Rathee होंगे Bigg Boss 18 के मिड वीक में एलिमिनेट? फैंस को लगा झटका\n\nZika Virus ने फिर बढ़ाई लोगों की चिंता, देश के इस राज्य से सामने आया नया मामला\n\nदिल्ली-नोएडा DND फ्लाईवे पर टोल वसूली रहेगी बंद, सुप्रीम कोर्ट ने इलाहाबाद हाई कोर्ट का फैसला ठहराया सही\n\nStree 2 से लेकर Bhool Bhulaiyaa 2 तक, 2024 में सबसे ज्यादा पॉपुलर हुईं ये 10 फिल्में\n\nहरियाणा के पूर्व सीएम ओमप्रकाश चौटाला का निधन, 89 साल में ली आखिरी सांस\n\nBhanu Saptami 2024: इस दिन है साल की आखिरी भानु सप्तमी, जानें सही तारीख से लेकर पूजा विधि और धार्मिंक महत्व\n\nIndian Airforce में अग्निवीरों की बंपर भर्तियां, जानें कौन कर सकता है आवेदन\n\nसेहत का खजाना है एवोकाडो, डाइट में शामिल करने से मिलेंगे ये चमत्कारी फायदे\n\nGood News: बेझिझक अंडा खा सकेंगे Cholesterol के मरीज, वैज्ञानिकों ने खोज निकाली नई तरकीब\n\nJaipur Petrol pump Blast: कैसे हुआ जयपुर में इतना बड़ा हादसा? CNG धमाके ने छीन ली कई जिंदगियां, जानें पूरी स्टोरी\n\nTeeth Sensitivity Remedies: ठंडा-गर्म खाने पर होती हैं दांतों में झनझनाहट, डेंटिस्ट के पास जाए बिना दूर कर सकते हैं समस्या\n\nIran के सुप्रीम लीडर खामनेई ने महिलाओं को बताया फूल, तो इजरायल ने क्यों याद दिलाई इस महिला की?\n\nपत्नी Aishwarya को प्रोटेक्ट करते दिखे अभिषेक बच्चन, तलाक की अफवाहों के बीच वायरल हुआ वीडियो\n\nमहाराष्ट्र के 3 हिल स्टेशन छुट्टियों के लिए सबसे खास डेस्टिनेशन\n\nFrizzy Hair की समस्या को ऐसे करें दूर, हेयर केयर के दौरान इन 5 बातों का रखें ध्यान\n\nViral: जानलेवा बना सेल्फी लेना, अचानक पीछे से आ गई ट्रेन फिर जो हुआ वह बेहद खतरनाक, देखें Video\n\nUP: हर हफ्ते 40 हजार कमाने का लालच देकर छात्रा को बुलाया मुंबई, अश्लील वीडियो बनाकर किया वायरल\n\n'कानून महिलाओं की भलाई के लिए है, पति को सताने के लिए नहीं', तलाक केस की सुनवाई के दौरान सुप्रीम कोर्ट का बड़ा बयान\n\nWinter Session: फिर छिनेगी Rahul Gandhi से सांसदी? बीजेपी सांसद ने दिया नोटिस, निलंबन की मांग\n\nPollution: दिल्ली की हवा में फिर से घुला जहर, स्कूल और दफ्तरों में लागू हुआ हाइब्रिड मोड, 450 के पार पहुंचा AQI\n\nCAT 2024 Results जारी, जानें नतीजों के बाद अब आगे क्या करना होगा\n\nVastu Tips: भूलकर भी किसी के घर से न लाएं ये 3 चीजें, हंसते खेलते परिवार में आ जाएगा तूफान\n\nसर्दियों में मक्के से रिप्लेस करें गेहूं का आटा, एक-दो नहीं, पूरे 5 फायदे देगी मक्के की रोटी\n\nPushpa 2 के डायरेक्टर Sukumar ने की भगदड़ में घायल बच्चे से मुलाकात, पैसों से की परिवार की मदद\n\nकौन है इस 'दिव्य' भैंस का मालिक?, दो गांवों के बीच मची लड़ाई, अब DNA टेस्ट कराएगी पुलिस, बड़ा ही दिलचस्प है ये केस\n\nViral: पुनीत सुपरस्टार प्लेन से आ रहा था बाहर, शख्स ने जड़ दिया थप्पड़, Video देख लोग बोले- हर जगह मार खाता रहता है\n\nUP: बिजली चोरी के आरोप में बुरे फंसे सांसद जिया उर रहमान, अब 19100000 का भरना पड़ेगा जुर्माना\n\nJaipur: जयपुर में पेट्रोल पंप पर बड़ा ब्लास्ट, 5 लोगों की मौत, 35 गंभीर घायल, 30 वाहन जले\n\nUP: कन्नौज में लाखों खर्च कर करवाया जेंडर चेंज, फिर रचाई शादी, जानें पूरा मामला\n\nभारत को आंखे दिखा रहे Bangladesh की पाकिस्तान संग पक रही खिचड़ी? काहिरा में मिले शहबाज और मोहम्मद यूनुस\n\nPushpa 2: 1500 करोड़ के क्लब में शामिल हुई अल्लू अर्जुन की फिल्म, फिर भी रह गई इस मूवी से पीछे\n\nNoida: स्कूल वॉशरूम के बल्ब होल्डर में मिला कैमरा, मोबाइल पर लाइव देखता पकड़ा गया डायरेक्टर\n\nSushant Singh Rajput की बहन ने लुटाया Ankita Lokhande पर प्यार, एक्ट्रेस के बर्थडे पर कही ये बात\n\nबढ़ा हुआ पेट बना युवक के लिए आफत, सीढ़ियों में फंसने का Video Viral\n\nReliance Jio ने किया JioTag Go डिवाइस को लॉन्च, अब एंड्रॉइड डिवाइस खोने का डर खत्म\n\nRussia Ukraine War: यूक्रेन ने मार गिराए उत्तर कोरिया के 100 सैनिक, अब क्या एक्शन लेंगे किम जोंग उन?\n\nअभिषेक-ऐश्वर्या के बीच है सब ठीक, तलाक की अफवाहों के बीच बच्चन परिवार संग दिखीं एक्ट्रेस\n\nबाहर कड़ाके की सर्दी फिर भी अंदर से गर्म रहेगा घर, बिना हीटर होगा काम, फॉलो करें ये 5 टिप्स\n\nWeather Update:अब शीतलहर बढ़ाएगी दिल्ली वालों की मुसीबत, यूपी-बिहार में तेजी से गिरने लगा पारा, जानिए आज के मौसम का हाल\n\nViral: दूसरी शादी का प्लान है क्या? पति के हेलमेट नहीं पहनने पर IPS ने ऐसे सिखाया सबक, देखें Video\n\nबुढ़ापे को दूर और आपको जवां रखेंगी ये 5 आदतें, जरूर फॉलो करें ये Anti Aging Habits\n\nसंभल: सपा सांसद जियाउर रहमान बर्क के खिलाफ FIR, 1 करोड़ 91 लाख का लगा जुर्माना, जानें क्या है मामला\n\nBihar Viral News: तीन बच्चों की मां और दो बच्चों के बाप के अजब प्यार की गजब कहानी, जानकर हैरान रह जाएंगे\n\nधक्का-मुक्की मामले में राहुल गांधी के खिलाफ FIR दर्ज, BNS की इन धाराओं में हुआ केस, जानें कितनी है सजा\n\nRashifal 20 December 2024: कन्या और वृश्चिक वालों को होगा धन लाभ, जानें आज मेष से मीन तक की राशियों का भाग्यफल\n\nSDM की गाड़ी का व्हील लॉक करना 6 कर्मचारियों को पड़ा भारी, दिनभर थाने में रखा बंद\n\nUS से सामने आया Bird Flu का पहला Severe Human Case, क्या महामारी बन सकती है ये बीमारी?\n\n50 पुरुष, 10 साल: कौन है Dominique Pelicot? जिसे अपनी बीवी के Mass Rape के लिए हुई 20 साल की सजा?\n\nसर्दियों में इस ड्राई फ्रूट को खाने से दूर रहेंगी बीमारियां, जानिए फायदे और कैसे करें इस्तेंमाल\n\nरोमियो पकड़ रही महिला पुलिस से ही कर दी छेड़छाड़, योगीराज में भी Moradabad में मनचलों के हौसले बुलंद\n\nमांसपेशियों, Immunity को रखना है मजबूत? ठंड में खाना शुरू कर दें ये 10 फल\n\nPunjab Terror Attack: पंजाब में 25 दिन में सातवां आतंकी हमला, पुलिस चौकी पर फेंका ग्रेनेड, पढ़ें अपडेट्स\n\nधक्कामुक्की मामले में राहुल गांधी के खिलाफ शिकायत, BJP सांसद का आरोप- मेरे साथ कुछ ऐसा हुआ...\n\nWinter Health: ठंड में खूब पी रहे हैं गुनगुना पानी? ये लोग करें अवॉइड, फायदे के बजाए पहुंचा सकता है नुकसान\n\n'वो लंपट छिछोरा...' Ranbir Kapoor को राम बनना 'शक्तिमान' को नहीं आ रहा रास! कह बैठे विवादित बात\n\nFarmer Protest: 'बुजुर्ग किसान भूखा है और आप सब सही बता रहे' किसान नेता डल्लेवाल की तबीयत बिगड़ने पर भड़का सुप्रीम कोर्ट, पढ़ें पूरी बात\n\nVirat Kohli का बच्चों की वजह से मेलबर्न एयरपोर्ट पर हुआ पत्रकार से झगड़ा, जानें पूरा विवाद\n\nसुनीता विलियम्स की धरती पर वापसी मार्च 2025 तक टली, आखिर क्यों मजबूर हुई NASA?\n\n'अंबेडकर के मुद्दे पर ध्यान भटकाना चाहती है BJP', धक्कामुक्की कांड पर बोले राहुल गांधी\n\nAtul Subhash Case: कहां है अतुल सुभाष का 4 साल का बेटा? पत्नी निकिता ने अब खुद बताई सच्चाई",
            "source": {
                "uri": "dnaindia.com",
                "dataType": "news",
                "title": "Daily News and Analysis (DNA) India"
            },
            "authors": [
                {
                    "uri": "मीना_परजापति@dnaindia.com",
                    "name": "मीना प्रजापति",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://cdn.dnaindia.com/sites/default/files/2024/12/20/7143756-sanjay-29.jpg",
            "eventUri": None,
            "sentiment": None,
            "wgt": 33,
            "relevance": 1
        },
        {
            "uri": "8429419373",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "09:42:33",
            "dateTime": "2024-11-26T09:42:33Z",
            "dateTimePub": "2024-11-26T09:42:01Z",
            "dataType": "news",
            "sim": 0.6196078658103943,
            "url": "https://www.aninews.in/news/world/asia/us-ambassador-to-india-pays-tributes-to-2611-martyrs20241126150730/",
            "title": "US Ambassador to India pays tributes to 26/11 martyrs",
            "body": "Mumbai (Maharashtra) [India], November 26 (ANI): The US Ambassador to India, Eric Garcetti on Tuesday paid his respects to the victims of the deadly 26/11 terror attacks at the Taj Mahal Palace Hotel in Mumbai.\n\nToday, on the 16th anniversary of the attack, Garcetti said that the US pledges to continue the fight against acts of terror with India.\n\nIn a post on X, he said, \"Today marks the 16th anniversary of the 26/11 terror attacks in Mumbai. We honor the memory of the victims lost and pledge to continue the fight against acts of terror together with the Government of India.\"\n\nEarlier in the day, remembering the victims of the 26/11 terror attack, Consul General of Israel for Midwest India in Mumbai, Kobbi Shoshani paid his tribute to the martyrs on Tuesday at Nariman House in Mumbai.\n\nRemembering when he came to Colaba a few days after the attacks, he told ANI, \"I was sent here at Nariman House in Colaba 2-3 days after the event took place here. I still remember the ammunition smell. It was very terrible.\"\n\nHe further said that the terrorists wanted to create fear and break the economy, however as he sees the bustling restaurants, he sees a victory against terrorism.\n\n\"When I see full restaurants and people walking, buying, shopping and roaming freely, I feel this is the biggest victory against terrorism. The aim of the terrorists was not to kill people, they wanted to create fear and break the economy but when I see restaurants, shops and people at the train stations and other places, I fully understand that we won against terrorism. India won against terrorism,\" he told ANI.\n\nMaharashtra Chief Minister Eknath Shinde on Tuesday paid floral tributes to the bravehearts at the Martyrs Memorial in Mumbai on the 16th anniversary of the 26/11 Mumbai terror attacks.\n\nDeputy Chief Ministers Devendra Fadnavis, Ajit Pawar and state's governor C P Radhakrishnan also paid tributes at the Martyrs' Memorial on the premises of the Commissioner's Office today. (ANI)",
            "source": {
                "uri": "aninews.in",
                "dataType": "news",
                "title": "Asian News International (ANI)"
            },
            "authors": [],
            "image": "https://d3lzcn6mbbadaf.cloudfront.net/media/details/ANI-20241126093657.jpg",
            "eventUri": "eng-10118763",
            "sentiment": -0.5686274509803921,
            "wgt": 33,
            "relevance": 1
        },
        {
            "uri": "8454858276",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-12",
            "time": "17:44:10",
            "dateTime": "2024-12-12T17:44:10Z",
            "dateTimePub": "2024-12-12T17:43:51Z",
            "dataType": "news",
            "sim": 0.6705882549285889,
            "url": "https://tjvnews.com/2024/12/jewish-community-center-targeted-in-attempted-terror-attack-in-cape-town/",
            "title": "Jewish Community Center Targeted in Attempted Terror Attack in Cape Town",
            "body": "President-Elect Trump Taps Arizona's Kari Lake as Director of the Voice of America\n\nA Jewish community center in Cape Town was targeted in an attempted terror attack last Friday, which was foiled when an explosive device was found on the building grounds before it had detonated.\n\nThe center houses the community's main institutions, and is across the street from the historic Gardens synagogue.\n\nThe South African Jewish Report reported:\n\nThe Chief Rabbi of South Africa, Dr. Warren Goldstein, condemned the attempted terror attack, and called out local officials for failing to speak out against it.\n\n\"As of this recording,\" he said Tuesday, \"there has been no public word to the best of my knowledge said on statements issued on behalf of the president of South Africa, Cyril Ramaphosa; the premier of the Western Cape [province], Alan Winde; or the mayor of Cape Town, Geordin Hill-Lewis and that itself speaks volumes. It's a disgrace.\"\n\n[Mayor Hill-Lewis was reported to have spoken out later that day, albeit in conditional terms: \"Should the SAPS investigation confirm that this was an attempted attack on the Jewish community, I know I would speak for all Capetonians in condemning such an attempt in the strongest possible terms.\"\n\nSouth Africa has accused Israel of \"genocide\" in international tribunals, and Cape Town in particular has a large and vocal anti-Israel movement.\n\nA large anti-Israel protest had been scheduled to be held outside the Jewish community offices earlier this week.",
            "source": {
                "uri": "tjvnews.com",
                "dataType": "news",
                "title": "The Jewish Voice"
            },
            "authors": [],
            "image": "https://tjvnews.com/wp-content/uploads/2024/12/Cape-Town-Joel-Pollak-Breitbart-News-640x480-1.jpg",
            "eventUri": "eng-10161185",
            "sentiment": -0.2235294117647059,
            "wgt": 33,
            "relevance": 18
        },
        {
            "uri": "8439140344",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-02",
            "time": "19:12:27",
            "dateTime": "2024-12-02T19:12:27Z",
            "dateTimePub": "2024-12-02T19:11:49Z",
            "dataType": "news",
            "sim": 0.4745098054409027,
            "url": "https://www.snopes.com//fact-check/wicked-ariana-grande-cancer/",
            "title": "Did Ariana Grande Receive Cancer Diagnosis During 'Wicked' Filming?",
            "body": "In November 2024, a series of TikTok posts alleged that singer and actress Ariana Grande was diagnosed with cancer (with some posts suggesting it was specifically lung cancer) while filming the movie adaptation of the Broadway musical \"Wicked.\" These videos offered no evidence to support the claim, nor has it been reported in any legitimate publications that she was diagnosed with cancer.\n\nFor instance, on Nov. 22, 2024, a TikTok post claimed that \"Ariana reportedly learned about her lung cancer diagnosis halfway through filming Wicked.\"\n\nThe rumors appeared to stem from ongoing fan speculation about Grande's health, fueled by discussions about her noticeably slender appearance during \"Wicked\" filming and subsequent media appearances. Posts on forums such as Reddit had voiced concerns over her health, particularly in regard to her weight loss, although they had not attributed it to cancer.\n\nGrande, however, has not spoken of the cancer rumors directly. In early November 2024, The New York Times published an interview with the actress and her \"Wicked\" co-star Cynthia Erivo, where they discussed contracting COVID-19 during production, but did not mention any cancer diagnosis. According to the outlet, the two performers shared:\n\nERIVO: And if there was time, we were not well. There was one time when I got Covid, there was another time when she got Covid.\n\nGRANDE: We only got sick once each, but both were before some of the most important works of the whole movie -- mine was the week before \"Popular.\" I came to set with a mask on my final days of recovery to learn the hallway finale, and no one liked this joke but I loved it so I'll tell it: We were in the dorm room together and I sang in her ear, \"Positive, you're going to be positive!\" But I wasn't positive anymore, don't worry! I took the test.\n\nERIVO: I got Covid the week before I shot \"Defying Gravity.\" It was literally like, \"Sit down, Cynthia, not yet.\"\n\nA review of Grande's public statements and social media activity revealed no mention of a cancer diagnosis. In 2023, Grande had addressed speculation about her health and diminished appearance in a video message to fans, warning against making assumptions about someone's health based on their appearance and stating that comparisons to her past physique reflected \"the unhealthiest version of [her] body.\"\n\nGrande's representatives did not respond to requests for comment about the cancer rumor. We will update you should we receive a response.\n\nIt is worth noting that Grande has participated in cancer awareness initiatives in the past. She performed at a 2014 Stand Up to Cancer telecast to raise funds in support of cancer research and treatment development, and was slated to appear at a 2018 event for the nonprofit F*** Cancer but reportedly pulled out shortly after the death of her ex-boyfriend, rapper Mac Miller, from an accidental drug overdose a few weeks before the event.\n\nThe TikTok cancer rumors gained traction partly due to fans speculating on Grande's weight loss and perceived fragility during filming of \"Wicked.\" Tabloids and entertainment outlets, including Daily Mail and HELLO!, published stories about her slender frame, though none provided evidence linking her appearance to a cancer diagnosis.\n\n\"Wicked,\" directed by Jon M. Chu and co-starring Erivo, is the first of a two-part adaptation of the Broadway musical of the same name. Grande's role as Galinda has kept her in the public eye throughout filming, which reportedly began in late-2022. Both Grande and Erivo both faced public scrutiny over their weight loss, which fueled rumors about their health.\n\nThere is no credible evidence to support the claim that Grande was diagnosed with cancer during the filming of \"Wicked.\" The rumor likely stemmed from baseless speculation about her weight loss and health. As such, we rated this claim unfounded.\n\nSnopes has previously fact-checked rumors about Grande, including the unproven claim she offered to pay for the funerals of the Manchester bombing victims following the terror attack at Manchester Arena where she had been performing at the time.",
            "source": {
                "uri": "snopes.com",
                "dataType": "news",
                "title": "Snopes"
            },
            "authors": [],
            "image": "https://mediaproxy.snopes.com/width/1200/https://media.snopes.com/2024/11/ariana_grande_unfounded_cancer_diagnosis.png",
            "eventUri": "eng-10134077",
            "sentiment": -0.207843137254902,
            "wgt": 32,
            "relevance": 1
        },
        {
            "uri": "8439219545",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-02",
            "time": "20:29:07",
            "dateTime": "2024-12-02T20:29:07Z",
            "dateTimePub": "2024-12-02T20:28:28Z",
            "dataType": "news",
            "sim": 0.6980392336845398,
            "url": "https://freebeacon.com/national-security/all-hell-to-pay-trump-warns-hamas-to-return-all-hostages-by-inauguration-day-or-get-hit-harder-than-anybody-has-been-hit/",
            "title": "'ALL HELL TO PAY': Trump Warns Hamas To Return All Hostages by Inauguration Day or Get 'Hit Harder Than Anybody Has Been Hit'",
            "body": "'Everybody is talking about the hostages ... but it's all talk, and no action,' president-elect writes in Truth Social post\n\nPresident-elect Donald Trump has a message for Hamas and its benefactors in Tehran: Release the hostages before Inauguration Day, or else.\n\nIn a Monday afternoon Truth Social post, Trump said that \"everybody is talking about the hostages who are being held so violently, inhumanely, and against the will of the entire World,\" but \"it's all talk, and no action!\" He went on to warn Hamas that there will be \"ALL HELL TO PAY\" if the remaining Israeli and American hostages, taken by the terror group on October 7, are not returned by the time he returns to the White House.\n\n\"Please let this TRUTH serve to represent that if the hostages are not released prior to January 20, 2025, the date that I proudly assume Office as President of the United States, there will be ALL HELL TO PAY in the Middle East, and for those in charge who perpetrated these atrocities against humanity,\" he wrote.\n\n\"Those responsible will be hit harder than anybody has been hit in the long and storied History of the United States of America,\" the president-elect went on. \"RELEASE THE HOSTAGES NOW!\"\n\nTrump's message came just hours after Israel confirmed that an American citizen who was believed to be held hostage in Gaza, Omer Maxim Neutra, was killed by Hamas during the Oct. 7 terror attack. One-hundred-one hostages remain in Hamas captivity, including at least seven American citizens, three of whom are believed to be dead.\n\nTrump's deadline may pressure Hamas into inking a long-elusive ceasefire agreement before the president-elect takes office. The Jewish state agreed last week to a 60-day ceasefire deal with Lebanese terrorist group Hezbollah, with White House national security adviser Jake Sullivan arguing that the move made a Hamas ceasefire \"more likely.\"\n\nIt's unclear, however, how long Israel's ceasefire with Lebanon will last. Israeli officials expect the fight against Hezbollah and Iran to continue once President Joe Biden leaves office, the Washington Free Beacon reported. Biden administration officials, meanwhile, are reportedly concerned that the deal could \"unravel\" even sooner as Hezbollah moves weapons into restricted areas in violation of the agreement, prompting Israeli strikes. Biden adviser Amos Hochstein told the Israelis that they are enforcing the ceasefire \"too aggressively,\" one Israeli official told Axios.",
            "source": {
                "uri": "freebeacon.com",
                "dataType": "news",
                "title": "Washington Free Beacon"
            },
            "authors": [
                {
                    "uri": "adam_kredo@freebeacon.com",
                    "name": "Adam Kredo",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://freebeacon.com/wp-content/uploads/2024/12/president-trump-meets-with-workers-in-white-house-on-economic-plan-scaled-e1733170616274.jpg",
            "eventUri": "eng-10137077",
            "sentiment": -0.1607843137254902,
            "wgt": 32,
            "relevance": 1
        },
        {
            "uri": "2024-12-573246090",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-11",
            "time": "22:14:13",
            "dateTime": "2024-12-11T22:14:13Z",
            "dateTimePub": "2024-12-11T22:03:52Z",
            "dataType": "news",
            "sim": 0.6784313917160034,
            "url": "https://www.ynetnews.com/article/byk1ifdnjx",
            "title": "Terrorist opens fire on bus near Jerusalem, 12-year-old seriously wounded",
            "body": "A 12-year-old boy was seriously wounded in a shooting targeting a bus near the Tunnel Checkpoint in Jerusalem, Israel's emergency medical service, Magen David Adom, reported late on Wednesday.\n\nThe IDF confirmed the incident as a terror attack. A 40-year-old woman sustained minor gunshot wounds, and two others were lightly wounded by shrapnel. All four victims were evacuated to the capital's Hadassah Ein Kerem Medical Center for treatment.\n\n*This is a breaking news story*\n\nGet the Ynetnews app on your smartphone: Google Play: https://bit.ly/4eJ37pE | Apple App Store: https://bit.ly/3ZL7iNv",
            "source": {
                "uri": "ynetnews.com",
                "dataType": "news",
                "title": "ynetnews"
            },
            "authors": [
                {
                    "uri": "elisha_ben_kimon@ynetnews.com",
                    "name": "Elisha Ben Kimon",
                    "type": "author",
                    "isAgency": False
                },
                {
                    "uri": "liran_tamari@ynetnews.com",
                    "name": "Liran Tamari",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://ynet-pic1.yit.co.il/picserver6/crop_images/2024/12/12/SJkf3Kv4kx/SJkf3Kv4kx_0_107_961_541_0_large.jpg",
            "eventUri": "eng-10165678",
            "sentiment": -0.3490196078431372,
            "wgt": 32,
            "relevance": 1
        },
        {
            "uri": "8425798228",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-23",
            "time": "20:15:58",
            "dateTime": "2024-11-23T20:15:58Z",
            "dateTimePub": "2024-11-23T20:15:13Z",
            "dataType": "news",
            "sim": 0.7686274647712708,
            "url": "https://www.jpost.com/diaspora/article-830415",
            "title": "We must protect those to safeguard Jewish life, from Amsterdam to UAE",
            "body": "Emissaries like Rabbi Zvi Kogan, who has gone missing in Dubai in a suspected terror attack, stand at the front lines of Jewish continuity and must be protected.\n\n\"When you build a new house, you shall make a parapet for your roof, so that you will not bring blood upon your house if anyone falls from it.\" (Deuteronomy 22:8)\n\nThe Torah's command to build a parapet isn't just ancient construction advice -- it's a moral imperative, a mandate to ensure safety in all aspects of life. It's as if the text is calling out to us across the millennia: guard your spaces, protect your people. But what happens when the roofs are guarded, yet the builders themselves are unprotected? What happens when the pillars of our communities -- the rabbis, teachers, and emissaries -- are left vulnerable to threats that transcend borders?\n\nThis week, we were forced to confront those questions chillingly.\n\nRabbi Zvi Kogan was a familiar figure on the streets of Dubai. The Israeli-born Chabad emissary, who once served in the IDF and later managed a supermarket, was known for his warmth and resilience. His days were spent greeting Jewish tourists at the kosher restaurant, organizing Torah classes, and offering solace to Gulf residents navigating Jewish life far from home. He was more than a rabbi; he was the heart of a budding Jewish community.\n\nAnd now, he is missing.\n\nKogan's disappearance on Thursday sent shockwaves through the Jewish world. His car was found abandoned an hour outside Dubai, and reports suggest Iranian operatives may have been involved. The suspects have fled to Turkey. For now, we don't know where he is -- or what happened to him. But we do know this: emissaries like Kogan, the lifeblood of global Jewish communities, are increasingly in danger.\n\nThis war isn't just against Israel. It's against Jews and Jewish values. And it's happening everywhere.\n\nFrom Dubai to Amsterdam: Jews under attack\n\nKogan's disappearance comes on the heels of other chilling events. Earlier this month, in Amsterdam, Jewish fans of Maccabi Tel Aviv FC were ambushed and beaten by pro-Palestinian mobs in what can only be described as a premeditated pogrom. Videos showed men being chased into canals, slashed with knives, and spat on. \"We were ambushed,\" one fan told Maariv. Another said, \"The police abandoned us.\"\n\nIn Crown Heights, a slashing attack rattled the Chabad-centered neighborhood. And in Chicago, a Jewish man on his way to the synagogue was shot by an assailant shouting Allahu Akbar. These incidents, far from isolated, form a disturbing trend: being visibly Jewish is a risk.\n\nThe Jewish principle of pikuach nefesh -- saving a life -- has never felt more urgent. \"Whoever saves one life, it is as if they have saved the entire world\" (Mishnah Sanhedrin 4:5) is not just a teaching but a rallying cry. Protecting the lives of Jewish leaders, emissaries, and communities is not optional; it is our collective obligation.\n\nStay updated with the latest news!\n\nSubscribe to The Jerusalem Post Newsletter\n\nSubscribe Now\n\nAs Ze'ev Jabotinsky warned, \"The Jewish people must stand guard over its safety and security. No one else will do it for us.\" His vision of Jewish self-reliance resonates as we face rising threats in an increasingly hostile world.\n\nA battle for the soul of Jewish life\n\nEmissaries like Kogan stand at the front lines of Jewish continuity. They are the keepers of tradition, the builders of community. They represent not only Jewish identity but its survival. And that makes them targets.\n\nRonald S. Lauder, president of the World Jewish Congress, recently urged Nordic governments to enhance security for Jewish institutions, calling it a \"battle of values and civilizations.\" His words echo globally. If Chabad rabbis are disappearing in Dubai and Jews are being beaten in Amsterdam, where is it safe to be Jewish?\n\nIn Washington, synagogues like Kesher Israel have ramped up security ahead of the High Holidays. Rusty Rosenthal, director of security at the Jewish Federation of Greater Washington, called it \"the Jewish Super Bowl\" of security preparation. Metal detectors, armed guards, and situational awareness training are now the norm. \"We don't want to lose what makes us special -- being warm and welcoming,\" one synagogue director said. But this balance is becoming harder to strike.\n\nWhat next?\n\nThe disappearance of Kogan is a wake-up call. It reminds us that Jewish leaders and institutions are at the forefront of this fight, often unprotected and vulnerable. Governments must act decisively. Communities must be vigilant. And Jewish organizations must prioritize security -- not as a reaction but as a constant state of readiness.\n\nAs Theodor Herzl said, \"It is true that our people need protection and support, but above all they need to begin to defend themselves.\" His words and Jabotinsky's vision stand as a call to action: to protect those who protect Jewish life, wherever they may be.\n\nThis is not just about security. It's about survival. It's about the values and resilience that define who we are as Jews. We cannot afford to falter. Kogan -- and all who stand at the front lines of Jewish life -- deserve nothing less.",
            "source": {
                "uri": "jpost.com",
                "dataType": "news",
                "title": "The Jerusalem Post"
            },
            "authors": [],
            "image": "https://images.jpost.com/image/upload/f_auto,fl_lossy/c_fill,g_faces:center,h_407,w_690/633086",
            "eventUri": "eng-10116262",
            "sentiment": -0.02745098039215688,
            "wgt": 32,
            "relevance": 1
        },
        {
            "uri": "8433426206",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-28",
            "time": "15:55:34",
            "dateTime": "2024-11-28T15:55:34Z",
            "dateTimePub": "2024-11-28T15:54:56Z",
            "dataType": "news",
            "sim": 0.9254902005195618,
            "url": "https://thewhistler.ng/benue-innoson-motor-attacks-peter-obi-raises-alarm-over-worsening-insecurity/",
            "title": "Benue/Innoson Motor Attacks: Peter Obi Raises Alarm Over Worsening Insecurity",
            "body": "Former presidential candidate of the Labour Party, Peter Obi has raised an alarm over worsening insecurity across the country warning the country may soon be overrun if not checked.\n\nObi in a statement on Thursday which he shared across his social media accounts lamented attacks on Benue State and Innoson Motors in Nnewi, Anambra State, describing them as worrisome.\n\nWhile scores were killed in Benue in the attacks a few days ago, the attack on Innoson Motors led to the kidnapping of three members of staff.\n\nObi decried the spate of attacks warning that at a time investors are supposed to remain in the country, they are leaving further worsening the economic situation.\n\nHe said it is very saddening and heartbreaking that the wave of insecurity has continued to sweep through every part of the country with no end in sight.\n\nThe situation, he said, has added to \"the harrowing hardship the people are going through yet they cannot even sleep with their two eyes closed.\n\n\"More heartbreaking is the fact that our critical infrastructure is often targeted by these merchants of terror who have no regard for human lives.\n\n\"Just a few days ago, I read a harrowing report about the killing of about 30 persons by terrorists, in separate attacks on communities in two Local Government Areas of Benue State.\n\n\"Yesterday, I was shocked by the reports of the unfortunate terror attack on the motorcycle showroom of Innoson Vehicle Manufacturing in Nnewi, Anambra State, where about 3 members of the staff were also kidnapped.\n\n\"One very pertinent question that has continued to bother every well-meaning Nigerian is: \"Where are we headed as a nation with this level of insecurity?\"\n\nThe ex-Anambra governor further lamented that it \"is even more worrisome and discouraging that, in the face of the severe economic hardship facing our nation, our productive business facilities are attacked.\n\n\"This is a time when foreign investors are leaving the country in their numbers; our few resilient local investors still have to face a frightening level of insecurity and other challenges for them to remain in business.\"\n\nHe supposed that the country \"must not continue to allow this mindless waste of human lives and attack on our businesses and critical infrastructure, across the country.\n\n\"We must end this monster of insecurity before we are all consumed.\"\n\nHe offered his sympathy saying \"I sincerely commiserate with all the victims of the terror attack in Benue, and every part of our nation.\n\n\"I also sympathize with Chief Innoson Chukwuma over the attack on his business facility. I urge the security agents to do their best in rescuing the kidnapped workers.\n\n\"Again, we must end insecurity in our nation before it ends us,\" Obi added.",
            "source": {
                "uri": "thewhistler.ng",
                "dataType": "news",
                "title": "The Whistler Nigeria"
            },
            "authors": [
                {
                    "uri": "isuma_mark@thewhistler.ng",
                    "name": "Isuma Mark",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://thewhistler.ng/wp-content/uploads/2023/04/Innoson_factory_entrance-1.jpg",
            "eventUri": "eng-10127596",
            "sentiment": -0.7803921568627451,
            "wgt": 32,
            "relevance": 18
        },
        {
            "uri": "8439035987",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-02",
            "time": "17:43:26",
            "dateTime": "2024-12-02T17:43:26Z",
            "dateTimePub": "2024-12-02T17:41:57Z",
            "dataType": "news",
            "sim": 0.6274510025978088,
            "url": "https://www.breitbart.com/politics/2024/12/02/white-house-on-biden-buying-anti-israel-book-he-reads-broadly/",
            "title": "White House on Biden Buying Anti-Israel Book: 'He Reads Broadly'",
            "body": "White House national security spokesman John Kirby told reporters on Air Force One en route to Angola on Monday that he could not explain why President Joe Biden had bought an anti-Israel book, except that he \"reads broadly.\"\n\nBiden was seen leaving a book store in Nantucket, Massachusetts, on Friday with his soon-to-be pardoned son, Hunter Biden, holding a book, The Hundred Years' War on Palestine, by anti-Israel author Rashid Khalidi.\n\nKhalidi recently claimed that Israel had no legal right to respond to the Hamas terror attack of October 7. He was also a close personal friend of President Barack Obama; the Los Angeles Times infamously covered up a video of Obama speaking at a farewell party for Khalidi, after it reported the existence of the video during the 2008 election.\n\nAsked about the book, Kirby said that he \"can't speak to why the president made that particular purchase ... but he reads broadly.\" Asked whether Biden was actually reading the book, Kirby said that he did not know the answer.\n\nHunter Biden attended a rally for Israel last year, but it is possible his views, and those of his father, have since changed. Khalidi himself said Biden had bought the book \"4 years too late\" to change his policies in a pro-Palestinian way.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/12/Joe-Biden-anti-Israel-book-Associated-Press-e1733155693677.jpg",
            "eventUri": "eng-10131205",
            "sentiment": -0.02745098039215688,
            "wgt": 31,
            "relevance": 1
        },
        {
            "uri": "8451239858",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-10",
            "time": "15:13:52",
            "dateTime": "2024-12-10T15:13:52Z",
            "dateTimePub": "2024-12-10T15:13:40Z",
            "dataType": "news",
            "sim": 0.7058823704719543,
            "url": "https://dronedj.com/2024/12/10/ndaa-drone-dji-autel-usnda/",
            "title": "USNDA praises FY25 NDAA for tackling Chinese drone risks",
            "body": "The United States National Drone Association (USNDA) has thrown its support behind the Fiscal Year 2025 National Defense Authorization Act (NDAA), lauding provisions aimed at weakening China's grip on the US drone market while strengthening domestic manufacturing. Representing a coalition of national security and defense professionals, the USNDA is a non-profit organization advocating for the safe and innovative use of drones in national security, public safety, and other critical sectors.\n\nNathan Ecelbarger, spokesman for USNDA's provisional Board of Directors, commends congressional leaders, including Sen. Rick Scott and Congresswoman Elise Stefanik, for championing provisions that enhance US security while bolstering the resilience of the nation's drone supply chains.\n\n\"While emerging drone technology continues to globally change the character of warfare and demonstrate critical security vulnerabilities across national security and defense spectrums, swift and coordinated actions must be taken to replace the pervasive monopoly of China's drone technology with an American drone industrial base. Simply put, regardless of security or supply chain concerns addressed in the 2025 NDAA, allowing Chinese drones flying in American skies represents an unnecessary and reversible risk.,\" Ecelbarger says.\n\nAt the core of the legislation are provisions targeting Chinese drone manufacturers like DJI and Autel Robotics. The act mandates that the Federal Communications Commission (FCC) list these companies and their affiliates on its Covered List within a year, unless national security agencies conclude they pose no risk.\n\nBeing placed on the Covered List would prevent these companies' drones from operating on US communications infrastructure, effectively banning new models from being imported into the country. These measures, USNDA argues, are crucial steps toward reducing dependence on foreign technology and mitigating potential security threats.\n\nRelated: DJI fires back at proposed US ban on Chinese drones\n\nThe NDAA also requires the Department of Defense (DoD) to craft a Resilient Supply Chain Strategy, specifically focused on domestic manufacturing of small uncrewed aerial systems (sUAS). This strategy aims to replace China's dominance with a secure, American-led industrial base.\n\nWhile USNDA applauds the steps taken in the FY25 NDAA, Ecelbarger cautions that these measures alone are insufficient. Pointing out the lack of contingency plans for drone-related threats, Ecelbarger notes, \"After 9/11, the FAA could ground all flights nationally. No such capability exists today for drones in the event of a coordinated terror attack.\"\n\nUSNDA is urging Congress to adopt a comprehensive approach to rebuild the US drone industrial base, ensuring it not only removes reliance on Chinese technology but also accelerates the development of secure, American-made alternatives.\n\nThe organization has outlined several recommendations, including:\n\nAs drone technology becomes increasingly embedded in multiple sectors, USNDA stresses the need for urgent, coordinated action across government, industry, and academia. \"Humble, coordinated action is essential to maintaining the safety and security of our nation,\" Ecelbarger sums up.",
            "source": {
                "uri": "dronedj.com",
                "dataType": "news",
                "title": "DroneDJ"
            },
            "authors": [
                {
                    "uri": "ishveena_singh@dronedj.com",
                    "name": "Ishveena Singh",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://i0.wp.com/dronedj.com/wp-content/uploads/sites/2/2024/08/usnda-united-states-national-drone-association.jpg?resize=1200%2C628&quality=82&strip=all&ssl=1",
            "eventUri": "eng-10158470",
            "sentiment": 0.4666666666666666,
            "wgt": 31,
            "relevance": 1
        },
        {
            "uri": "8430602636",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-27",
            "time": "01:26:01",
            "dateTime": "2024-11-27T01:26:01Z",
            "dateTimePub": "2024-11-27T01:24:56Z",
            "dataType": "news",
            "sim": 0.8588235378265381,
            "url": "https://www.aninews.in/news/world/europe/mp-cm-mohan-yadav-pays-tributes-on-the-2611-mumbai-terror-attacks-anniversary-in-london20241127064921/",
            "title": "MP CM Mohan Yadav pays tributes on the 26/11 Mumbai Terror Attacks anniversary in London",
            "body": "London [UK], November 27 (ANI): Madhya Pradesh Chief Minister Mohan Yadav was invited by the High Commission of India in the UK to a commemorative ceremony marking the anniversary of the 26/11 Mumbai terror attacks.\n\nThe Chief Minister was formally invited by the High Commission of India to a commemorative ceremony held at India House. The event was a poignant remembrance of one of the most tragic terrorist attacks in Indian history, the press statement noted.\n\nDuring the ceremony, the Chief Minister delivered a deeply reflective address that captured the collective pain and memory of the devastating terror attack. His speech acknowledged the profound impact of the event, recognising two distinct groups of witnesses: those who experienced the horror firsthand during the actual attacks, and the millions of citizens who watched the traumatic events unfold through television broadcasts.\n\nCM Yadav's remarks were characterised by a tone of solemnity and hope, particularly when he expressed his heartfelt condolences for those who lost their lives during the terrible incident. His words aimed to honour the memory of the victims and underscore the resilience of those affected by the tragedy, the press statement observed.\n\nFollowing his address, CM Yadav toured an exhibition specifically curated at India House to commemorate the event. This exhibition featured photographs that provided a visual narrative and context to the attack, according to the press statement.\n\nThe visit concluded with a comprehensive tour of the India House, allowing the Chief Minister to engage more deeply with the memorials and to reflect on the significance of the day.\n\nThe event represented a moment of collective remembrance, reflection, and tribute to the victims of the 26/11 Mumbai terror attacks, emphasizing the importance of never forgetting such significant historical moments.\n\nCM Yadav also spoke to ANI.\n\n\"26/11 is the most unfortunate incident in the history of our country, especially from the point of view of national security for the people and the government\". He expressed condolences for people who were killed during the heinous attacks. (ANI)",
            "source": {
                "uri": "aninews.in",
                "dataType": "news",
                "title": "Asian News International (ANI)"
            },
            "authors": [],
            "image": "https://d3lzcn6mbbadaf.cloudfront.net/media/details/ANI-20241127011850.jpg",
            "eventUri": "eng-10123566",
            "sentiment": -0.4509803921568627,
            "wgt": 30,
            "relevance": 1
        },
        {
            "uri": "8429009037",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-11-26",
            "time": "04:20:21",
            "dateTime": "2024-11-26T04:20:21Z",
            "dateTimePub": "2024-11-26T04:18:48Z",
            "dataType": "news",
            "sim": 0.4745098054409027,
            "url": "https://www.breitbart.com/middle-east/2024/11/25/exclusive-idf-official-hezbollah-ran-away-from-us-in-southern-lebanon/",
            "title": "Exclusive -- IDF Official: Hezbollah Ran Away from Us in Southern Lebanon",
            "body": "Hezbollah fled from Israel Defense Forces (IDF) soldiers in southern Lebanon, refusing to confront them in direct combat during the two months in which Israel has been on the ground there, removing terrorist border positions.\n\nA senior military official from the IDF, speaking to Breitbart News on condition that his name not be used, said: \"They [Hezbollah] left the battle zone ... Unlike their ethos, they didn't stay and fight. Not in the numbers that they were claiming ... Every face-to-face encounter ended with the elimination of the enemy force.\"\n\nThe official's claim is corroborated by the relatively low number of combat deaths among IDF soldiers in southern Lebanon. While there have been occasional ambushes or skirmishes, Hezbollah fighters have typically abandoned their positions.\n\nHezbollah positions had also sustained nearly 11 months of airstrikes by Israel, after Hezbollah began the conflict by firing on Israel's border communities on October 8, 2023, in solidarity with the Hamas terror attack the day before.\n\nIsrael also eliminated the senior echelon of Hezbollah commanders, and destroyed the group's communications network, in its daring use of exploding pagers and walkie-talkies before beginning its ground assault in September.\n\nThe fact that the IDF has routed Hezbollah, and that the terror group is unable to defend southern Lebanon, is a blow to the prestige of the organization, which claimed for years that its fighters were tougher than IDF soldiers.\n\nA 60-day ceasefire is expected to be accepted by both sides in the coming days, bringing the current phase of the conflict to a close. Hezbollah may attempt to rebuild, but the strategic balance has been changed in Israel's favor.",
            "source": {
                "uri": "breitbart.com",
                "dataType": "news",
                "title": "Breitbart"
            },
            "authors": [
                {
                    "uri": "joel_b_pollak@breitbart.com",
                    "name": "Joel B. Pollak",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://media.breitbart.com/media/2024/11/IMG_9584.jpg",
            "eventUri": "eng-10120785",
            "sentiment": -0.4431372549019608,
            "wgt": 30,
            "relevance": 1
        },
        {
            "uri": "2024-12-571978767",
            "lang": "eng",
            "isDuplicate": False,
            "date": "2024-12-10",
            "time": "18:20:34",
            "dateTime": "2024-12-10T18:20:34Z",
            "dateTimePub": "2024-12-10T18:12:11Z",
            "dataType": "news",
            "sim": 0,
            "url": "https://www.abc.net.au/news/2024-12-11/melb-synagogue-terror-attack-fire-adass-israel-torah-scrolls/104705852",
            "title": "Inside the fight to save holy scrolls damaged in synagogue blaze",
            "body": "To Daniel Aghion, a burnt Torah scroll represents more than just a ruined object.\n\n\"It's a symbol of survival,\" the president of the Executive Council of Australian Jewry said.\n\nAs he digested the damage done to Torah scrolls in Friday's torching of the Adass Israel Synagogue in Ripponlea, Mr Aghion couldn't help but think of all the times history has repeated itself.\n\nEvents such as Kristallnacht, or the 'Night of Broken Glass', where the Nazi regime unleashed violence across Germany and its territories in November 1938.\n\nThe Nazis destroyed Torah scrolls and synagogues, among other Jewish symbols.\n\n\"Ultimately, it represents the Holocaust, and that's why it is so emotional and significant to see that,\" Mr Aghion said.\n\nSix scrolls were damaged in the suspected terror attack in Melbourne.\n\nThis week, Jewish ritual scroll repairer and ordained scribe Rabbi Eli Gutnick is also feeling the weight of history.\n\nThere aren't many like him. To become qualified, he had to study for a number of years before his certification in Israel.\n\nHe has the difficult task of repairing scrolls damaged in the synagogue fire, two of which are dedicated to people who died in the Holocaust.\n\n\"Each one has its own story,\" he said.\n\n\"The extent of the damage is still going to be verified, and we're going to do whatever we can to save them.\"\n\nFireproof safe prevents destruction\n\nThe scrolls were contained in a fireproof safe, which was installed after an arson attack on the same synagogue in 1995.\n\nAs stated in newspaper articles at the time, none of the 20 scrolls were destroyed, and the fireproofing was installed as a preventative measure.\n\nWhile the safe offered some protection during last Friday's blaze, radiant heat and water from dousing the fire caused damage to the delicate parchment.\n\nThe congregation found the scrolls soaking wet and sprung into action, quickly laying them out to dry, which Mr Gutnick said had prevented more damage.\n\n\"They got fans and air conditioners and set up the tables,\" he said.\n\n\"It was all done very quickly. Instead of dwelling on ... the shock, everyone just jumped into action.\n\nThere's a lot at stake for Mr Gutnick, who said the scrolls that were unable to be repaired must be buried in a ceremony similar to a funeral.\n\n\"As a scribe my role is to try to get these scrolls in the best condition that possibly can be and to avoid having to bury them,\" he said.\n\n\"That's devastating for the community when you have to do like a funeral procession ... we're working to avoid that.\"\n\nHandwritten for at least a year\n\nTorah scrolls are considered the holiest object in the Jewish religion, containing the text of the five books of Moses, otherwise known as the Old Testament.\n\nMr Gutnick said these scrolls were handwritten by a scribe, usually in Israel, with a feather quill on a parchment made from organic material that was difficult to write on.\n\nThis entire process, which involves writing around 300,000 letters in Hebrew, can take a significant amount of time.\n\nThe scrolls are often made in memory of a deceased family member, and hold a monetary value of at least $100,000.\n\n\"You've basically got to pay someone for a year or two to sit and write them so they're quite valuable,\" Mr Gutnick said.\n\nOnce donated or lent to a synagogue, they're stored in an 'Ark', or ornate cabinet.\n\nThey're then taken to be read during holy services.\n\nBenjamin Klein, a board member of the Adass Israel Synagogue, said his family owned one of the damaged scrolls.\n\nHis father-in-law donated it to the synagogue in memory of his parents, who had recently died.\n\n\"Very much it's grief, that's what the feeling is at the moment,\" Mr Klein said.\n\nMr Gutnick said the \"huge emotional connection\" to these scrolls had been evident when people attended his office.\n\n\"It's very important that people realise that there's a strong emotional and spiritual connection.\"\n\nSaving the scrolls will be a complex process. Mr Gutnick said while some words could be rewritten, there were rules preventing other words from being replaced.\n\nAs counter-terrorism teams investigate the arson, Mr Gutnick said it was still too early to determine whether the scrolls could be repaired.",
            "source": {
                "uri": "abc.net.au",
                "dataType": "news",
                "title": "Australian Broadcasting Corporation"
            },
            "authors": [
                {
                    "uri": "syan_vallance@abc.net.au",
                    "name": "Syan Vallance",
                    "type": "author",
                    "isAgency": False
                },
                {
                    "uri": "madi_chwasta@abc.net.au",
                    "name": "Madi Chwasta",
                    "type": "author",
                    "isAgency": False
                }
            ],
            "image": "https://live-production.wcms.abc-cdn.net.au/55fdbf426034b706b672f461434c37a4?impolicy=wcms_watermark_news&cropH=864&cropW=1536&xPos=0&yPos=592&width=862&height=485&imformat=generic",
            "eventUri": None,
            "sentiment": -0.2705882352941177,
            "wgt": 29,
            "relevance": 1
        }
    ]
