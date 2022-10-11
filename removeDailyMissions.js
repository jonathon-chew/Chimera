const eventTitles = document.getElementsByClassName("eventCardHeaderSet");
const numberOfEvents = eventTitles.length
const checkBox = document.getElementsByClassName("eventCardCompletedToggleButton");
//const cardName = document.getElementsByClassName("eventCardContainer");

setInterval(function () {for (let i = 0; i < numberOfEvents; i++){
    if(eventTitles[i].innerHTML === "Sever"){
        checkBox[i].click()
    };
}},1000)
