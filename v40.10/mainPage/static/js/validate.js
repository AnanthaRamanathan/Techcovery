$(document).ready(function(){
    
    var error = document.getElementById("emailError")           
    $(".email").on("input",function(){
        
        if ($(this).val() == ""){
            $("#emailError").hide();
            $(".email").css({border:""});
        }
            
        else {
            if (checkEmail($(this).val())){
                $(".email").css({border:""});
                $("#emailError").hide();
            }
            else{
                $("#emailError").show();
                $(".email").css({border: "2px solid red"});
                
            }
        }
    })
    
    function checkEmail(txt) {
        var patt = /[a-z0-9._%+-]+@[a-z0-9.-]+\.[com - in]{2,3}$/;
        if(patt.test(txt))
            return true;
        else
            
            return false;
    }
})

$(document).ready(function(){
                
    $(".Your_Linkedin_Profile").on("input",function(){
        
        if ($(this).val() == ""){
            $("#passiveLinkedinError").hide();
            $("#activeLinkedinError").hide();
            $(".Your_Linkedin_Profile").css({border:""});
        }
            
        else {
            if (checklinkedin($(this).val())){
                $("#passiveLinkedinError").hide();
                $("#activeLinkedinError").hide();
                $(".Your_Linkedin_Profile").css({border:""});
            }
                
            else{
                $("#passiveLinkedinError").show();
                $("#activeLinkedinError").show();
                $(".Your_Linkedin_Profile").css({border: "2px solid red"});

            }
              
        }
    })
    
    function checklinkedin(txt) {
        var patt = /[https]+:["//www"]+.["linkedin"]+.["com"/]/;
        
        
        if(patt.test(txt))
            return true;
        else
            return false;
    }


    
         
}) 

