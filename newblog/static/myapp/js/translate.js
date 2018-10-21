$(document).ready(function(){


    
    $('#word_button').on('click',function(){
        
        var context  = $('#context_word').val()

        ul = '/word_translates/?word='+context
        

        $.ajax({
            type:'get',
            url:ul,
            dateType:'json',
            success:function(data,status){

                var d = data['data']
                var result = ''
                for (i in d){
                    result = result + d[i] + '\n'
                }
                $('#word_context').text(result)
                

            }


        })




    

    });





    $('#sentence_button').on('click',function(){
        
        var context  = $('#context_sentence').val()

        ul = '/sentence_translates/?sentence='+context
        
        

        $.ajax({
            type:'get',
            url:ul,
            dateType:'json',
            success:function(data,status){

                var d = data['data']
                var result = ''
                for (i in d){
                    
                    result = result + d[i] + '\n'
                }
                
                $('#setence_context').text(result)
                

            }


        })




    

    })




})