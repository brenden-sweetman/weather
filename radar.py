from PIL import Image
from urllib import request
import datetime


def buildRadar(radarLocation):
    # Request images
    request.urlretrieve("http://radar.weather.gov/ridge/Warnings/Short/"+radarLocation+"_Warnings_0.gif", "radar/"+radarLocation+"/Warnings.gif")
    request.urlretrieve("http://radar.weather.gov/ridge/RadarImg/N0R/"+radarLocation+"_N0R_0.gif", "radar/"+radarLocation+"/Radar.gif")


    base = Image.open("radar/"+radarLocation+"/Topo.jpg").convert("RGBA")
    warnings = Image.open("radar/"+radarLocation+"/Radar.gif").convert("RGBA")
    radar = Image.open("radar/"+radarLocation+"/Warnings.gif").convert("RGBA")
    county = Image.open("radar/"+radarLocation+"/County.gif").convert("RGBA")
    highways = Image.open("radar/"+radarLocation+"/Highways.gif").convert("RGBA")
    cities = Image.open("radar/"+radarLocation+"/Cities.gif").convert("RGBA")

    base.paste(warnings, (0,0), warnings)
    base.paste(county, (0,0), county)
    base.paste(highways, (0,0), highways)
    base.paste(radar, (0,0), radar)
    base.paste(cities, (0,0), cities)

    now = datetime.datetime.now()
    base.save("radar/"+radarLocation+"/Radar_Composite_Current.png")
    #base.save("radar/"+radarLocation+"/Radar_Composite_"+now.strftime("%S%M%H%d%m%Y")+".png")

def getDailyOutlook():
    #Request Images
    request.urlretrieve("https://www.spc.noaa.gov/products/outlook/day1otlk.gif","dailyOutlook/outlook.gif")
    outlook = Image.open("dailyOutlook/outlook.gif").convert("RGBA")
    outlook.save("dailyOutlook/Outlook_Current.png")
    #outlook.save("dailyOutlook/Outlook"+datetime.datetime.now().strftime("%d%m%Y")+".png")

def mesoscale(mesoLocation):
    # Request Images
    request.urlretrieve("https://www.spc.noaa.gov/exper/mesoanalysis/"+mesoLocation+"/rgnlrad/rgnlrad.gif","mesoscale/"+mesoLocation+"/rnglrad.gif")
    request.urlretrieve("https://www.spc.noaa.gov/exper/mesoanalysis/"+mesoLocation+"/scp/scp.gif","mesoscale/"+mesoLocation+"/scp.gif")


    base = Image.open("mesoscale/"+mesoLocation+"/base.gif").convert("RGBA")
    population = Image.open("mesoscale/"+mesoLocation+"/population.gif").convert("RGBA")
    highways = Image.open("mesoscale/"+mesoLocation+"/highways.gif").convert("RGBA")
    radar = Image.open("mesoscale/"+mesoLocation+"/rnglrad.gif").convert("RGBA")
    scp = Image.open("mesoscale/"+mesoLocation+"/scp.gif").convert("RGBA")

    base.paste(population, (0,0), population)
    base.paste(radar, (0,0), radar)
    base.paste(scp, (0,0), scp)
    base.paste(highways, (0,0), highways)

    now = datetime.datetime.now()
    base.save("mesoscale/"+mesoLocation+"/meso_scp_Current.png")
    #base.save("mesoscale/"+mesoLocation+"/meso_scp_"+now.strftime("%S%M%H%d%m%Y")+".png")


if __name__=="__main__":
    buildRadar("EAX")
    getDailyOutlook()
    mesoscale("s14")
