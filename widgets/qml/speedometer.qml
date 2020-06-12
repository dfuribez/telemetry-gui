import QtQuick 2.0
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4

Rectangle {
    id: root
    width: 400
    height: 400
    color: "black"
    anchors.fill: parent
    
    Text {
        // property string value: "0Km/h"
        objectName: "text"
        anchors.left: parent.left
        anchors.right: parent.right
        text: "100"
        color: "red"
        y: root.height * 0.2
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: parent.width * 0.1
    }

    CircularGauge {
        id: gauge
        objectName: "gauge"

        property real gauge_value: 100
        property real ticks_values: 50
        property real max_value: 100
        property real min_value: 0
        property string min_color: "red"
        property string max_color: "lawngreen"

        anchors.fill: parent
        value: gauge_value

        maximumValue: max_value
        minimumValue: min_value

        style: CircularGaugeStyle {

            foreground: Item {
                Rectangle {
                    width: outerRadius * 0.2
                    height: width
                    radius: width / 2
                    
                    anchors.centerIn: parent
                }
            }

            tickmarkLabel: Text {
                text: styleData.value
                color: styleData.value >= 50 ? gauge.min_color : gauge.max_color
                antialiasing: true
            }

        }
    }
}