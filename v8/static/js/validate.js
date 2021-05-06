$(document).ready(function(){
                
    $(".email").on("input",function(){
        
        if ($(this).val() == "")
            $(".email").css({backgroundColor:""});
        
        else {
            if (checkEmail($(this).val()))
                $(".email").css({backgroundColor:""});
            else
                $(".email").css({backgroundColor:"rgb(236, 110, 110)"});
                ("**length of your password must be between 3 and 10");

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
        
        if ($(this).val() == "")
            $(".Your_Linkedin_Profile").css({backgroundColor:""});
        
        else {
            if (checklinkedin($(this).val()))
                $(".Your_Linkedin_Profile").css({backgroundColor:""});
            else
                $(".Your_Linkedin_Profile").css({backgroundColor:"rgb(236, 110, 110)"});

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

