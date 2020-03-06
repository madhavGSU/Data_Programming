import math;



latitudeAtlanta = 33.7242700 
longitudeAtlanta = -84.5785800 
latitudeOrlando = 28.3855400
longitudeOrlando = -81.5058900 
latitudeSavannah = 32.1672300 
longitudeSavannah = -81.1998900 
latitudeCharlotte = 35.2072400 
longitudeCharlotte = -80.9567600 
radiusOfEarth = 6371.01



atlantaOrlandoDist=radiusOfEarth*math.acos(math.sin(latitudeAtlanta)*math.sin(latitudeOrlando)+math.cos(latitudeAtlanta)*math.cos(latitudeOrlando)*math.cos(longitudeAtlanta-longitudeOrlando));
orlandoSavannahDist=radiusOfEarth*math.acos(math.sin(latitudeOrlando)*math.sin(latitudeSavannah)+math.cos(latitudeOrlando)*math.cos(latitudeSavannah)*math.cos(longitudeOrlando-longitudeSavannah));
savannahCharlotteDist=radiusOfEarth*math.acos(math.sin(latitudeSavannah)*math.sin(latitudeCharlotte)+math.cos(latitudeSavannah)*math.cos(latitudeCharlotte)*math.cos(longitudeSavannah-longitudeCharlotte));
atlantaCharlotteDist=radiusOfEarth*math.acos(math.sin(latitudeAtlanta)*math.sin(latitudeCharlotte)+math.cos(latitudeAtlanta)*math.cos(latitudeCharlotte)*math.cos(longitudeAtlanta-longitudeCharlotte));
atlantaSavannahDist=radiusOfEarth*math.acos(math.sin(latitudeAtlanta)*math.sin(latitudeSavannah)+math.cos(latitudeAtlanta)*math.cos(latitudeSavannah)*math.cos(longitudeAtlanta-longitudeSavannah));

avg2=(atlantaOrlandoDist+orlandoSavannahDist+atlantaSavannahDist)/2;
avg1=(atlantaSavannahDist+atlantaCharlotteDist+savannahCharlotteDist)/2;

area1=math.sqrt(avg1* (avg1-atlantaSavannahDist) * (avg1-savannahCharlotteDist) * (avg1-atlantaCharlotteDist));
area2=math.sqrt(avg2* (avg2-orlandoSavannahDist) * (avg2-atlantaSavannahDist) * (avg2-atlantaOrlandoDist))

print("The area between these four cities is", round(area1+area2,2), "square kilometres.");

