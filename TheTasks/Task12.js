

const book={

title :"Java",

description :"Java Program",

numberOfPages: 20,

authour :"(string)",

reading :false,
getboo: function() { 
    this.reading = ! this.reading
    return this.reading
}


}
console.log(` initial value is : ${book.reading}`)
console.log(`after calling funtion ${ book.getboo()}`)