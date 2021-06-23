
//var listt= document.getElementById('list1')
var flag=0;
$("#list1").on('click','#complete1',function(){
    flag=1;
    $(this).addClass('hide');
    $(this).siblings("#update1").addClass('hide');
    $(this).siblings("#content1").addClass('strike');
    

});



    
    


    
    



