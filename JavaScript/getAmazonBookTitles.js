//Whilst this does work, this has been replaced with the ability to read the xml file from the Kindle app

let allBookTitles = []

for (let index = 1; index < 15; index++) {
  
    window.location.href = `https://www.amazon.co.uk/hz/mycd/digital-console/contentlist/booksPurchases/dateDsc?pageNumber=${index}`

    let bookTitles = document.querySelectorAll('.digital_entity_title')

  for (let i = 0; i < bookTitles.length; i++) {
    let bookTitle = bookTitles[i];

      allBookTitles.push(bookTitle.innerHTML)

  }
  
}

console.log(allBookTitles.join(", "))
