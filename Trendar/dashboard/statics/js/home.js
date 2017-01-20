/**
 * Created by I321310 on 12/30/2016.
 */
 function allowDrop(ev)
{
ev.preventDefault();
};

function drag(ev)
{
ev.dataTransfer.setData("Text",ev.target.id);
};

function drop(ev)
{
ev.preventDefault();
var data=ev.dataTransfer.getData("Text");
ev.target.appendChild(document.getElementById(data));
};





/**
 * Created by I321310 on 1/13/2017.
 */

var rankUrl = 'http://127.0.0.1:8000/api/in_t/';
var tfUrl = 'http://127.0.0.1:8000/api/in_e/';

function display1(urlAddress){
    $.ajax({
        type:'GET',
        url:urlAddress,
        dataType:'json',
        contentType:"application/json",
        success:function(data){
            var myChart = echarts.init(document.getElementById('word-cloud'));
            var topPos = [];
            $.each(data,function(index,item){
                topPos.push({
                    name:(item.name),
                    value:parseInt(item.rank * 1000)
                })
            });
//指定图表的配置项和数据
            var option={
                tooltip:{},
                series:[{
                    type:'wordCloud',
                    gridSize:7,
                    sizeRange:[10,18],
                    rotationRange:[0,0],
//                    shape:'circle',
                    width: '150%',
                    height: '100%',
                    textStyle:{
                        normal:{
                            color:function(){
                                return'rgb('+[
                                        Math.round(Math.random()*255),
                                        Math.round(Math.random()*255),
                                        Math.round(Math.random()*255)
                                    ].join(',')+')';
                            }
                        },
                        emphasis:{
                            shadowBlur:10,
                            shadowColor:'#333'
                        }
                    },
                    data:topPos
                }]
            };

//使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);

//更新Header
            $('#top-phrases h3').text(((urlAddress == rankUrl)?'TextRank':'TF-IDF')+'算法词云图');

//更新top-positives
            var dlist = $('#top-positives dl');
            dlist.html('');
            if(topPos.length<5)
                dlist.text('Failed to load data');
            else{
                for(var i=0;i<5;i++){
                    dlist.append($('<dt></dt>').text(topPos[i].name.toString()));
                    dlist.append($('<dd></dd>').text(topPos[i].value.toString()));
                }
            }
        },
        error:function(data){
            alert("error");
        }
    });
};


//function display2(){
//    $.ajax({
//        type:'GET',
//        url:
//        dataType:'json',
//        contentType:"application/json",
//        success:function(data){
//           // var myChart = echarts.init(document.getElementById('word-cloud'));
//            var topComplaints = [];
//            $.each(data,function(index,item){
//                topComplaints.push({
//                //[{"modelNumber":"FS-0029","point1":"尺码小"，"value1":"59","point2":"白颜色不好看","value2":"25","point3":"镶边不好看","value3":"20","point4":"金属钉","value4":"9"}，
//                //{"modelNumber":"FT-0015N","point1":"尺码小"，"value1":"88","point2":"红颜色不好看","value2":"34","point3":"做工粗糙","value3":"15","point4":"金属钉","value4":"9"}]
//                    modelNumber:(item.modelNumber),
//                    point1:(item.point1),
//                    point2:(item.point2),
//                    point3:(item.point3),
//                    point4:(item.point4),
//                    value1:parseInt(item.value1 * 1000),
//                    value2:parseInt(item.value2 * 1000),
//                    value3:parseInt(item.value3 * 1000),
//                    value4:parseInt(item.value4 * 1000)
//                })
//            });
//            $("#topcomplaints1").append(
//                   // "<tr>"
//                    //+"<td>"+ objectList[i].feature
//                    //+ "<td>"+""+objectList[i].number
//                   // + "</tr>"
//                   "型号:"+topComplaints[0].modelNumber
//                   +"<dt>"+topComplaints[0].point1+"</dt>"
//                   +"<dd>"+topComplaints[0].value1+"</dd>"
//                   +"<dt>"+topComplaints[0].point2+"</dt>"
//                   +"<dd>"+topComplaints[0].value2+"</dd>"
//                   +"<dt>"+topComplaints[0].point3+"</dt>"
//                   +"<dd>"+topComplaints[0].value3+"</dd>"
//                   +"<dt>"+topComplaints[0].point4+"</dt>"
//                   +"<dd>"+topComplaints[0].value4+"</dd>"
//                    );
//            $("#topcomplaints2").append(
//                   // "<tr>"
//                    //+"<td>"+ objectList[i].feature
//                    //+ "<td>"+""+objectList[i].number
//                   // + "</tr>"
//                   "型号:"+topComplaints[1].modelNumber
//                   +"<dt>"+topComplaints[1].point1+"</dt>"
//                   +"<dd>"+topComplaints[1].value1+"</dd>"
//                   +"<dt>"+topComplaints[1].point2+"</dt>"
//                   +"<dd>"+topComplaints[1].value2+"</dd>"
//                   +"<dt>"+topComplaints[1].point3+"</dt>"
//                   +"<dd>"+topComplaints[1].value3+"</dd>"
//                   +"<dt>"+topComplaints[1].point4+"</dt>"
//                   +"<dd>"+topComplaints[1].value4+"</dd>"
//                    );
//
////            var option={
////                tooltip:{},
////                series:[{
////                    type:'wordCloud',
////                    gridSize:7,
////                    sizeRange:[10,18],
////                    rotationRange:[0,0],
//////                    shape:'circle',
////                    width: '150%',
////                    height: '100%',
////                    textStyle:{
////                        normal:{
////                            color:function(){
////                                return'rgb('+[
////                                        Math.round(Math.random()*255),
////                                        Math.round(Math.random()*255),
////                                        Math.round(Math.random()*255)
////                                    ].join(',')+')';
////                            }
////                        },
////                        emphasis:{
////                            shadowBlur:10,
////                            shadowColor:'#333'
////                        }
////                    },
////                    data:topPos
////                }]
////            };
//
////使用刚指定的配置项和数据显示图表。
////            myChart.setOption(option);
//
//        },
//        error:function(data){
//            alert("error");
//        }
//    });
//};

var psgContent = [
    "Passage 0 Passage 0 Passage 0 Passage 0",
    "Passage 1 Passage 1 Passage 1 Passage 1",
    "Passage 2 Passage 2 Passage 2 Passage 2",
    "Passage 3 Passage 3 Passage 3 Passage 3",
    "Passage 4 Passage 4 Passage 4 Passage 4",
    "Passage 5 Passage 5 Passage 5 Passage 5",
    "Passage 6 Passage 6 Passage 6 Passage 6",
    "Passage 7 Passage 7 Passage 7 Passage 7",
    "Passage 8 Passage 8 Passage 8 Passage 8",
    "Passage 9 Passage 9 Passage 9 Passage 9"
];

function autoScroll() {

//init: load
//scroll
//when the bottom of the first one reaches the top line, delete in the array and append a new one
//when hover, stop scroll

    var li = $('#top-hl div ul li');
    var totalHeight =
        parseInt(li.css('margin-top'), 10) +
        parseInt(li.css('margin-bottom'), 10) +
        parseInt(li.css('border-top'), 10) +
        parseInt(li.css('border-bottom'), 10) +
        parseInt(li.css('padding-top'), 10) +
        parseInt(li.css('padding-bottom'), 10) +
        parseInt(li.css('height'), 10);

    var ul = $('#top-hl div ul');
    ul.html('');
    var maxRowInList = 6;
    $('#top-hl div').css('height', ((maxRowInList - 1) * totalHeight).toString() + 'px')

    var cells = [];
    psgContent.forEach(function (item) {
        cells.push($('<li>').text(item));
    });

    var cellsInList = [];
    for(var i = 0; i < maxRowInList; i++){
        cellsInList[i] = cells[i];
    }

    cellsInList.forEach(function (item, index) {
        item.appendTo(ul);
    });

    ul.animate({top:'-='+totalHeight.toString()+'px'},2000,function () {
        cellsInList.splice(0,1);
        cellsInList.push(cells[6]);
        ul.html('');
        ul.css('top','0');
        cellsInList.forEach(function (item, index) {
            item.appendTo(ul);
        });
    });

    ul.animate({top:'-='+totalHeight.toString()+'px'},2000,function () {
        cellsInList.splice(0,1);
        cellsInList.push(cells[7]);
        ul.html('');
        ul.css('top','0');
        cellsInList.forEach(function (item, index) {
            item.appendTo(ul);
        });
    });

    ul.animate({top:'-='+totalHeight.toString()+'px'},2000,function () {
        cellsInList.splice(0,1);
        cellsInList.push(cells[8]);
        ul.html('');
        ul.css('top','0');
        cellsInList.forEach(function (item, index) {
            item.appendTo(ul);
        });
    });
    // ul.animate({top:'-='+totalHeight.toString()+'px'},2000);
    //
    // ul.animate({top:'-='+totalHeight.toString()+'px'},2000);
    //
    // ul.animate({top:'-='+totalHeight.toString()+'px'},2000);
};





$(document).ready(function(){
        display1(rankUrl);
        autoScroll();
//        display2();
//        $('.switch input').change(function(){
//                if(this.checked)
//                    display1(tfUrl);
//                else
//                    display1(rankUrl);
//            }
//        );

    }
);




