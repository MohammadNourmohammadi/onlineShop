function updatePrice() {
    if (document.getElementById("post_tehran").checked == true) {
        document.getElementById("final_price").innerText = Number(document.getElementById("cart_total_price").innerText) + 35000;
    } else {
        document.getElementById("final_price").innerText = Number(document.getElementById("cart_total_price").innerText)  + 30000;
    }
    //
    // if (document.getElementById("item2").checked == true && document.getElementById("item1").checked == true) {
    //     price = 17;
    // } else if(document.getElementById("item2").checked == true) {
    //     price = 7
    // }
    //
    // if (document.getElementById("item3").checked == true && document.getElementById("item1").checked == true && document.getElementById("item2").checked == true) {
    //     price = 20;
    // } else if (document.getElementById("item3").checked == true && document.getElementById("item1").checked == true) {
    //     price = 13
    // } else if (document.getElementById("item3").checked == true && document.getElementById("item2").checked == true) {
    //     price = 10
    // } else if (document.getElementById("item3").checked == true){
    //     price = 3
    // }


}