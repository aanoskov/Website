let formElement = document.getElementById("knopka");
formElement.onclick = function() {
  cnt=1;
  number=eval(document.getElementsByClassName("number")[0]["children"][0].value);
  days=eval(document.getElementsByClassName("days")[0]["children"][0].value);
  if (days==2){
    cnt=number*3990;
  }
  else {
    if (days==3){
      cnt=number*5290;
    }
    else{
      if (days==5){
        cnt=number*6590;
      }
      else{
        cnt=number*7390;
      }
    }
  }
  alert(
    "Уважаемы(-ая), " +
      document.getElementsByClassName("name")[0]["children"][0].value +
      "\n" +
      "мы позвоним по номеру " +
      document.getElementsByClassName("phone-num")[0]["children"][0].value +
      
      " в течении часа\n" +
      "Количество людей: "+
      document.getElementsByClassName("number")[0]["children"][0].value +
      "\n" +
      "Количество дней: "+
      document.getElementsByClassName("days")[0]["children"][0].value +
      "\n" +
      "Ваша стоимость составит: " +
      cnt
  );
};