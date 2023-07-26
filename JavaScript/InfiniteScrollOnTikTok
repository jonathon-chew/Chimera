function infiniteScroll(){
const nextVideo = document.querySelector('[aria-label="Go to next video"]')

setInterval(function() {
let videoTime = document.getElementsByClassName('tiktok-o2z5xv-DivSeekBarTimeContainer e1rpry1m1')
let currentVT = videoTime[0].innerHTML

let currentVTArray = currentVT.split("/")

let timePlayer = currentVTArray[0]
let totalTime = currentVTArray[1]

if (timePlayer === totalTime){
    nextVideo.click()
}  
  
}, 100)


}

infiniteScroll()
