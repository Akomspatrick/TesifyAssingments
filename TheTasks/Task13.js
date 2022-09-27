const books =[
    {
    title: 'Think like a Man ',
    description:'Better ways to handle Life situation',
    numberOfPages: 25,
    author:'Joe John',
    reading:false,
},
 {  title: 'Today and Next Tomorrow',
    description:'Life and chances ',
    numberOfPages: 70,
    author:'Brown Bobby',
    reading:true,
 },

   { title: 'A-Z of Software Testing Practices',
     description: ' basis of software testing ',
    numberOfPages: 100,
    author:'Francine Rivers',
    reading:false,
}
]
for (let i = 0; i < books.length; i++) {
    if (books[i].reading==true)
    {
    console.log(books[i])
    }
}