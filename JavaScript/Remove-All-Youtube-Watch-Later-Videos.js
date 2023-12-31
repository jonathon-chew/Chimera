//paste into console log
/* setInterval(function() {
	document.querySelector('#contents button[aria-label="Action menu"]').click();
	var things = document.evaluate('//span[contains(text(),"Watch later")]',document,null,XPathResult.ORDERED_NODE_SNAPSHOT_TYPE,null);
		for (var i = 0; i < things.snapshotLength; i++) {
		    things.snapshotItem(i).click();
		}		
}, 1000);*/

//paste into console log
setInterval(function() {
	document.querySelector('#contents button[aria-label="Action menu"]').click();
	var things = document.querySelector("#items > ytd-menu-service-item-renderer:nth-child(3) > tp-yt-paper-item")
	things.snapshotItem(i).click();
	}, 1000);
