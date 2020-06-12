import QtQuick 2.0
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4

Rectangle {
    width: 400
    height: 400
    color: "black"
    anchors.fill: parent
    
    CircularGauge {
        id: gauge
        objectName: "gauge"

        property real gauge_value: 100

        anchors.fill: parent
        value: gauge_value
        style: CircularGaugeStyle {

            foreground: Item {
                Rectangle {
                    width: outerRadius * 0.2
                    height: width
                    radius: width / 2
                    
                    anchors.centerIn: parent
                }
            }

        }
    }
}