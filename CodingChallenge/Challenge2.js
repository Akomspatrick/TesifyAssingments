console.log("2. Create a length converter function(Centimeters TO Meters)")
console.log('-----------------------------------------------------------')
const valueInCm =2000
//CmToMetersConverter = function(cm){
//    meter = cm * 0.01;
//    return meter
//}
//Answer = CmToMetersConverter(valueInCm)

//ggggggg
CmToMetersConverter = (cm)=> cm * 0.01;
console.log(`The value of ${valueInCm}cm in  Meters is  ${CmToMetersConverter(valueInCm)}`)
