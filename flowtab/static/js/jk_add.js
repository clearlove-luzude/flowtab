

//展示域名
   $.ajax({
            type: 'get',
            url:/DomainName_info_shijie/,
            dataType: "json",
            success:function(data){
                console.log("success");
                var str = "";
                var html1 = "";
                var form = layui.form;
                for(var a = 0; a<data.length;a++){
                    html1 += '<dd lay-value="' + data[a].id + '">' + data[a].name + '</dd>';
                    str+='<option value = '+data[a].id+'>'+data[a].name+'</option>';
                }
                //console.log(html1);
                $("#yuming").next().children().eq(1).html(html1);
                $("#yuming").html(str);
                form.render();
                }
        })

//添加监控
  $("#monitor_add").click(function(){
            var id = document.getElementById("yuming").selectedIndex;
            var name = document.getElementById("yuming").options[id].text;
            var value = document.getElementById("value").value;
            var jk_id = document.getElementById("jkpro").selectedIndex;
            var jk_name = document.getElementById("jkpro").options[jk_id].text;
            var emails =document.getElementById("email").value;
            console.log(name,value,jk_name,emails);
            var data = {"id":id, "domianname" : name, "value" : value, "jk_name" : jk_name, "email": emails};
            if( value == null || value == "" ||  emails == null || emails == "" ){
                alert ('不能为空');
            }else{
            console.log(data);
            $.ajax({
                type: 'GET',
                url:/monitor_add/,
                data: data ,//{"domianname" : name, "starttime" : startTime, "endtime" : endTime},
                dataType: "json",
                success:function(data){
                console.log(data);
                alert (JSON.stringify(data));
                var m_rows = data.rows;
                console.log(data["accmsg"]);
                if ( data["accmsg"] == "添加成功!"){
                    xadmin.close();
                        // 可以对父窗口进行刷新
                    xadmin.father_reload();
                    //if (top.location != self.location){
                    //    top.location = self.location;
                    //    location.href = '/monitor/';
               // }
                }
    }
    })
    }
    })

