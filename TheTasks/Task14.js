const books =
[
{
    title :"Java1",
    description: "(string)",
    numberOfPages :10,
    authour: "O Patrick",
    reading :false,
    toggleReadingStatus : function()
    { this.reading = !this.reading;  return this.reading}    
},{
    title :"Java2",
    description: "(string)",
    numberOfPages :10,
    authour: "O Patrick",
    reading :true,
    toggleReadingStatus : function()
    { this.reading = !this.reading;  return this.reading}    
},
{
    title :"Java3",
    description: "(string)",
    numberOfPages :10,
    authour: "O Patrick",
    reading :false,
    toggleReadingStatus : function()
    { this.reading = !this.reading;  return this.reading}    
},{
    title :"Java4",
    description: "(string)",
    numberOfPages :10,
    authour: "O Patrick",
    reading :true,
    toggleReadingStatus : function()
    { this.reading = !this.reading;  return this.reading}    
}
]
readbooks=books.filter(e=>e.reading===true)
readbooks.forEach(e=>console.log(e))