
$(document).ready(function(){
var data;
    $.ajax({
      type: "GET",  
      url: "links1.csv",
      dataType: "text",       
      success: function(response)  
      {
        data = $.csv.toArrays(response);
        console.log(data);
        addToCards(data);
      }   
    });
    function addToCards(data) {
      var i = 0;
        $.each(data, function( index, row ) {
          //bind header
          if(index == 0) {
            //do nothing
            var dataa = "sata";
            console.log(dataa);
          } else {
            $.each(row, function( index, colData ) {
                 var html = "<div class=\"col-lg-4 col-sm-6 portfolio-item\"><div class=\"card h-100\"><a href=\"#\"><img class=\"card-img-top\" src=\"duck.jpg\" alt=\"\"></a><div class=\"card-body\"><h4 class=\"card-title\"><a href=\"";
                let words=colData.split("/");
                html += colData;
                html+= "\">"
                if(!words[2].localeCompare("www.hackerearth.com")){
                  html+=words[5];
                }
                else{
                  html+=words[4];
                }
                html+="</a></h4><p class=\"card-text\">Click the above link for further info</p></div></div></div>"//
                if(i<6 ){
                  $('#pager').append(html);
                }
                else if(i>=6 && i<12){
                  $('#page1').append(html);
                }
                else if(i>=12 && i<18){
                  $('#page2').append(html);
                }
                else if(i>=18 && i<24){
                  $('#page3').append(html);
                }
                else{
                  $('#page4').append(html);
                }
            
            i++;
            });
          }
        });
        
      }
      }); 