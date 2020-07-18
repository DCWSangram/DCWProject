function validation()
    {
        var regex = /^[6789]\d{9}/;
        var regex2 = /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/;
        var email = document.getElementById('email');
        var fullname = document.getElementById('fullname');
        var pwd1 = document.getElementById('pwd1');
        var pwd2 = document.getElementById('pwd2');
        var mobile = document.getElementById('mobile');
        var add = document.getElementById('add');

        if (email.value == "")
        {
            document.getElementById("email1").innerHTML = "**Please fill this field";
            email.style.border="1px red solid";
            return false;
        }
        else{
            document.getElementById("email1").innerHTML = "";
            email.style.border="1px solid black";
        
        }
        if (email.value.indexOf("@") <= 0)
        {
            document.getElementById("email1").innerHTML = "**Invalid @ Postion...";
            email.style.border="1px red solid";
            return false;
        }
        else{
            document.getElementById("email1").innerHTML = "";
            email.style.border="1px solid black";
        }
        if ((email.value.charAt(email.value.length-4) != '.') && (email.value.charAt(email.value.length-4) != '.'))
        {
            document.getElementById("email1").innerHTML = "**Email address should ends with '.com/.in'";
            email.style.border="1px red solid";
            return false;
        }
        else{
            document.getElementById("email1").innerHTML = "";
            email.style.border="1px solid black";
        }

        if (fullname.value == "")
        {
            document.getElementById("fullname1").innerHTML = "**Please provide some name";
            fullname.style.border="1px red solid";
            return false;
        }
        else{
            document.getElementById("fullname1").innerHTML = "";
            fullname.style.border="1px solid black";
        }
        if(!regex2.test(fullname.value)){
            document.getElementById("fullname1").innerHTML = "**Please provide a Valid Name";
            fullname.style.border="1px red solid";
            return false;
        }
        
        if (pwd1.value == "")
        {
            document.getElementById("pwd11").innerHTML = "**Please provide Password";
            pwd1.style.border="1px red solid";
            return false;
        }
        else{
            document.getElementById("pwd11").innerHTML = ""
            pwd1.style.border="1px solid black"
        }
        if (pwd2.value == "")
        {
            document.getElementById("pwd22").innerHTML = "**Please confirm Password";
            pwd2.style.border="1px red solid";
            return false;
        }
        else{
            document.getElementById("pwd11").innerHTML = ""
            pwd1.style.border="1px solid black"
        }
        if (pwd1.value.length < 8)
        {
            document.getElementById("pwd11").innerHTML = "**Password should contain at least 8 characters";
            pwd1.style.border="1px red solid";
            return false;
        }
        else{
            document.getElementById("pwd11").innerHTML = ""
            pwd1.style.border="1px solid black"
        }
        if (pwd1.value !== pwd2.value)
        {
            document.getElementById("pwd22").innerHTML = "**Password does not macth";
            document.getElementById("pwd11").innerHTML = "**Password does not macth";
            pwd1.style.border="1px red solid";
            return false;
        }
        else{
            document.getElementById("pwd11").innerHTML = ""
            pwd1.style.border="1px solid black"
        }
        if (mobile.value == "")
        {
            document.getElementById("mobile1").innerHTML = "**Please enter your Mobile Number";
            mobile.style.border="1px red solid";
            return false;
        }
        if (mobile.value.length != 10)
        {
            document.getElementById("mobile1").innerHTML = "**Invalid Mobile Number...provide 10 digits Mobile Number";
            mobile.style.border="1px red solid";
            return false;
        }
        if (regex.test(mobile.value)){
            document.getElementById("mobile1").innerHTML = "";
            mobile.style.border="1px black solid";
        }
        else{
            document.getElementById("mobile1").innerHTML = "**Invalid Mobile Number..";
            mobile.style.border="1px red solid";
            return false;
        }
        
       
    }