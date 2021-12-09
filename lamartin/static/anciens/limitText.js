$(document).ready(function(){
  
    $('.limit').each(function (f) {
  
        var newstr = $(this).text().substring(0,120)+"...";
        $(this).text(newstr);
  
      });
  })