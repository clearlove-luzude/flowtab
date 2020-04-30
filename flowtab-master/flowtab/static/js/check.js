    layui.use(['layer', 'element', 'form'], function () {
        var element = layui.element;
        var layer = layui.layer;
        var form = layui.form;

        //select自适应
        function select_adaption(select_input) {
            var div_width = select_input.prev().outerWidth(true)
            select_input.css('padding-left', (parseInt(div_width) + 6) + 'px')
            select_input.val('')
        }

        //select模糊搜索
        function vagueselect(obj, type) {
            var select_input = obj.find('[name="select_input"]')
            var select_show = obj.find('[name="select_show"]')

            function getdataList() {
                var parms = new Object();
                parms["keyword"] = select_input.val();
                parms["csrfmiddlewaretoken"] = $("[name = 'csrfmiddlewaretoken']").val()
                $.ajax({
                    cache: true,
                    type: "POST",
                    url: '/test/',
                    data: parms,
                    async: false,
                    success: function (data) {
                        var json = $.parseJSON(data);
                        var html
                        if (type == 'multiple') {
                            select_input.prev().children().each(function () {
                                for (var i = 0; i < json.data_list.length; i++) {
                                    if (json.data_list[i].ID == $(this).attr('belong_id')) {
                                        //删除已选选项
                                        json.data_list.splice(i, 1)
                                    }
                                }
                            })
                        }
                        if (json.data_list.length > 0) {
                            //将获得的数据填充到下拉的数据框里
                            select_show.children().first().hide().nextAll().remove()
                            for (var i = 0; i < json.data_list.length; i++) {
                                html = '<dd lay-value="' + json.data_list[i].ID + '" class="">' + json.data_list[i].Name + '</dd>';
                                select_show.append(html)
                            }
                        }
                        else {
                            if (parms["keyword"].length > 0) {
                                //如果为搜索到匹配项显示
                                select_show.children().first().hide().nextAll().remove()
                                html = '<dd lay-value="无" class="layui-select-tips">无该匹配项</dd>';
                                select_show.append(html)
                            }
                            else {
                                //如果未输入关键字复原样式
                                select_show.children().first().show().nextAll().remove()
                            }
                        }
                    },
                    error: function (request) {
                        layer.msg("Connection error", {icon: 2});
                    }
                });
            }

            //输入框聚焦事件
            select_input.focus(function () {
                obj.find('.layui-form-select').addClass('layui-form-selected')
                getdataList()
            })
            //输入框失去焦点事件
            select_input.blur(function () {
                var input_dom = this
                $(document).on('click', function (event) {
                    var dom = select_show[0]
                    if (event.target !== input_dom && event.target !== dom) {
                        obj.find('.layui-form-select').removeClass('layui-form-selected')
                    }
                })
            })
            //当案件松开时
            select_input.keyup(function () {
                getdataList()
            })
            if (type == 'single') {
                obj.delegate('dd', 'click', function () {
                    if ($(this).index() > 0) {
                        $(this).siblings().removeClass('layui-this')
                        $(this).addClass('layui-this')
                        select_input.val($(this).text())
                        select_input.attr('id', $(this).attr('lay-value'))
                        obj.find('.layui-form-select').removeClass('layui-form-selected')
                    }
                });
            }
            else if (type == 'multiple') {
                //为选择项绑定点击事件
                obj.delegate('dd', 'click', function () {
                    if ($(this).index() > 0 && $(this).text() !== '无该匹配项') {
                        $(this).siblings().removeClass('layui-this')
                        $(this).addClass('layui-this')
                        var temp = '<a class="select_a" belong_id="' + $(this).attr('lay-value') + '" ><i class="layui-icon" style="cursor: pointer;" name="select_del">ဆ</i>' + $(this).text() + '</a>'
                        console.log(temp)
                        select_input.prev().append(temp)
                        console.log(select_input.prev())
                        select_adaption(select_input)
                        obj.find('.layui-form-select').removeClass('layui-form-selected')
                        obj.parent().parent().next().find('input').attr('disabled', false)
                        obj.parent().parent().next().find('select').attr('disabled', false)
                        form.render()
                    }
                });
            }
        }

        //删除选项统一接口
        $('body').delegate('[name="select_del"]', 'click', function () {
            var select_input = $(this).parent().parent().next()
            if ($(this).parent().siblings().length == 0) {
                $(this).parents(':eq(5)').nextAll().find('input').attr('disabled', true)
                $(this).parents(':eq(6)').next().find('input').attr('disabled', true)
                $(this).parents(':eq(6)').next().find('select').attr('disabled', true)
                form.render()
            }
            $(this).parent().remove()
            select_adaption(select_input)
        });

        vagueselect($('[name="single_select"]'), 'single')
        vagueselect($('[name="multiple_select"]'), 'multiple')
    });

