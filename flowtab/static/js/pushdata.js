   $.ajax({
            type: 'get',
            url:/DomainName_info/,
            dataType: "json",
            success:function(data){
                console.log("success");
                var str = "";
                for(var a = 0; a<data.length;a++){
                    console.log(data[a]);
                    str+='<option value = '+data[a].id+'>'+data[a].name+'</option>';
                }
                $("#yuming").html(str);
                }
        })


           var myChart = echarts.init(document.getElementById('main1'));
       // var myChart = ec.init(document.getElementById("main"))
        // 基于准备好的dom，初始化echarts实例
        // 指定图表的配置项和数据
         var option = {
            tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                }
            },
            grid: {
                top: '5%',
                right: '2%',
                left: '1%',
                bottom: '10%',
                containLabel: true
            },
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data: [],
                }
            ],
            yAxis : [
                {
                    type : 'value'
                }
            ],
            series : [
                {
                    name:'http',
                    type:'line',
                    areaStyle: {normal: {}},
                    data: [],
                    smooth: true,
                },
                 {
                    name:'https',
                    type:'line',
                    areaStyle: {normal: {}},
                    data: [],
                    smooth: true,
                }
            ]
        };
        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        // 基于准备好的dom，初始化echarts实例
        var myChart2 = echarts.init(document.getElementById('main2'));
        // 指定图表的配置项和数据
        var option = {
            tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                }
            },
            grid: {
                top: '5%',
                right: '2%',
                left: '1%',
                bottom: '10%',
                containLabel: true
            },
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data: [],
                }
            ],
            yAxis : [
                {
                    type : 'value'
                }
            ],
            series : [

                {
                    name:'http',
                    type:'line',
                    areaStyle: {normal: {}},
                    data:[],
                    smooth: true,
                     },
                     {
                    name:'https',
                    type:'line',
                    areaStyle: {normal: {}},
                    data:[],
                    smooth: true,
                    },
            ]
        };
        myChart2.setOption(option);



        $("#searchData").click(function(){
            //var myChart;
            var flowarr_time = new Array;
            var flowarr_http = new Array;
            var flowarr_https = new Array;
            var traarr_time = new Array;
            var traarr_http = new Array;
            var traarr_https = new Array;
            var id = document.getElementById("yuming").selectedIndex;
            var name = document.getElementById("yuming").options[id].text;
            var startTime =document.getElementById("start").value;
            var endTime =document.getElementById("end").value;
            var data_id = document.getElementById("datainterval").selectedIndex;
            var datainterval = document.getElementById("datainterval").options[data_id].text;
            console.log(name,startTime,endTime,datainterval);
            var data = {"domianname" : name, "starttime" : startTime, "endtime" : endTime, "datainterval": datainterval};
            if( startTime == null || startTime == "" ||  endTime == null || endTime == "" ){
                alert ('请选择时间间隔');
            }else{
            console.log(data);
            $.ajax({
                type: 'GET',
                url:/Get_datas/,
                data: data ,//{"domianname" : name, "starttime" : startTime, "endtime" : endTime},
                dataType: "json",
                success:function(data){
                 console.log(data);
                 var flowdata = data[''+name+''][''+'flow'+''];
                 var tradata = data[''+name+''][''+'tra'+''];
                 //var flowarr_time = new Array;
                 //var flowarr_http = new Array;
                 //var flowarr_https = new Array;
                 for(var a = 0; a<flowdata.length;a++){
                    flowarr_time.push(flowdata[a][''+'times'+'']);
                    flowarr_http.push(flowdata[a][''+'http'+'']);
                    flowarr_https.push(flowdata[a][''+'https'+'']);
                 }
                // var traarr_time = new Array;
                 //var traarr_http = new Array;
                 //var traarr_https = new Array;
                 console.log(flowarr_http);
                 for(var a = 0; a<tradata.length;a++){
                    traarr_time.push(tradata[a][''+'times'+'']);
                    traarr_http.push(tradata[a][''+'http'+'']);
                    traarr_https.push(tradata[a][''+'https'+'']);
                 }

        // 使用刚指定的配置项和数据显示图表。
                //myChart.hideLoading();
                myChart.setOption({
tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                }
            },
            grid: {
                top: '5%',
                right: '2%',
                left: '1%',
                bottom: '10%',
                containLabel: true
            },
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data: flowarr_time
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    axisLabel: {
                      formatter: function (value) {
                        if(!value) return ''
                                                if(value >= 1073741824){
                                                    return (parseInt(value / 1073741824) + "GB");
                                                } else if (value >= 1048576) {
                                                    return (parseInt(value / 1048576) + "MB");
                                                } else if (value >= 1024) {
                                                    return (parseInt(value / 1024) + "KB");
                                                } else {
                                                    return value + "B";
                                                }
                      }
                  }
},
                                    {
                  type: 'value',
                  name: '字节',
                  axisLabel: {
                      formatter: '{value} %'
                  }
                                    },

            ],
            series : [
                {
                    name:'http',
                    type:'line',
                    areaStyle: {normal: {}},
                    data: flowarr_http,
                    smooth: true,
                },
                 {
                    name:'https',
                    type:'line',
                    areaStyle: {normal: {}},
                    data: flowarr_https,
                    smooth: true,
                }
            ]
                })
                //渲染
                //myChart.hideLoading();
                myChart2.setOption({
 tooltip : {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    label: {
                        backgroundColor: '#6a7985'
                    }
                }
            },
            grid: {
                top: '5%',
                right: '2%',
                left: '1%',
                bottom: '10%',
                containLabel: true
            },
            xAxis : [
                {
                    type : 'category',
                    boundaryGap : false,
                    data: traarr_time,
                }
            ],
            yAxis : [
                {
                    type : 'value',
                    axisLabel: {
                      formatter: function (value) {
                        if(!value) return ''
                                                if(value >= 1073741824){
                                                    return (parseInt(value / 1073741824) + "GB");
                                                } else if (value >= 1048576) {
                                                    return (parseInt(value / 1048576) + "MB");
                                                } else if (value >= 1024) {
                                                    return (parseInt(value / 1024) + "KB");
                                                } else {
                                                    return value + "B";
                                                }
                      }
                  }
                    },
                                    {
                  type: 'value',
                  name: '字节',
                  axisLabel: {
                      formatter: '{value} %'
                  }
                                    },
            ],
            series : [

                {
                    name:'http',
                    type:'line',
                    areaStyle: {normal: {}},
                    data:traarr_http,
                    //data:traarr_http,
                    smooth: true,
                     },
                     {
                    name:'https',
                    type:'line',
                    areaStyle: {normal: {}},
                    data:traarr_https,
                    smooth: true,
                    },
            ]
                })
                 //渲染
                }
            })
            }//判断时间
        })
        //}
