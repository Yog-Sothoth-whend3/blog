$(document).ready(function(){
    $('#sent').on('click',function(){
        var username =$('#username').val()
        if (username == '')
        {
            alert('用户名不能为空')
        }
        else{

            ul = '/search_username/?username=' + username
            $.ajax({

                type:"get",
                url:ul,
                dataType :"json",
                success:function(data,status){
                var d = data['data'];
                if (d[0] == "该用户名已存在"){

                    alert(d[0])
                }
                else{

                    var email = $('#email').val()
                    el = '/emails/?info='+email
                    $.ajax({
                        type:"get",
                        url:el,
                        dataType :"json",
                        success:function(data,status){
                            var e = data['data'];
                            alert(e[0])
                        }
                        
                        

                    })


                }



                }
    
            })
        }
        
        

    })


})