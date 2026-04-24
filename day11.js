document.getElementById("btn").addEventListener("click", ()=>{
    console.log("Button was clicked!");
    const newimg = document.createElement("btn");
    newimg.setAttribute("serc" , "https://images.pexels.com/photos/851151/pexels-photo-851151.jpeg?cs=srgb&dl=pexels-siddharth-shrivastav-290620-851151.jpg&fm=jpg");newimg.setAttribute("alt" , "Image");
    
    document.getElementById("Content").appendChild(newimg);
}
)
