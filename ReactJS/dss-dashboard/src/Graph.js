import { color } from 'd3-color';
import React, { Component } from 'react';

import LiquidFillGauge from 'react-liquid-gauge';
import firebase from './firebase'

var weightMax = 16;
var distanceMax = 50;

class Graph extends Component {
    constructor(props) {
        super(props);

        this.state = {
            value: 0
        }
    };

    componentDidMount() {
        const db = firebase.firestore();

        db.collection("User").doc("KitchenShelf").onSnapshot((doc) => {
            var data = doc.data()[this.props.param];
            if (this.props.param === "Distance") {
                data = (distanceMax - data) / distanceMax * 100;
                if (data < 0) {
                    data = 0;
                }
            } else {
                data = data / weightMax * 100;
            }

            this.setState({
                value: data
            });
        });
    };

    calcFillColor(value) {
        if (value < 33 || value == null) {
            return '#ff0000';
        } else if (value > 66) {
            return '#7CFC00';
        } else {
            return '#ffff00'
        }

    }

    render() {
        const radius = 200;
        const fillColor = this.calcFillColor(this.state.value);
        const gradientStops = [
            {
                key: '0%',
                stopColor: color(fillColor).darker(0.5).toString(),
                stopOpacity: 1,
                offset: '0%'
            },
            {
                key: '50%',
                stopColor: fillColor,
                stopOpacity: 0.75,
                offset: '50%'
            },
            {
                key: '100%',
                stopColor: color(fillColor).brighter(0.5).toString(),
                stopOpacity: 0.5,
                offset: '100%'
            }
        ];

        return (
            <div>
                <LiquidFillGauge
                    style={{ margin: '50px' }}
                    width={radius * 2}
                    height={radius * 2}
                    value={this.state.value}
                    percent="%"
                    textSize={1}
                    textOffsetX={0}
                    textOffsetY={0}
                    textRenderer={(props) => {
                        const value = Math.round(props.value);
                        const radius = Math.min(props.height / 2, props.width / 2);
                        const textPixels = (props.textSize * radius / 2);
                        const valueStyle = {
                            fontSize: textPixels
                        };
                        const percentStyle = {
                            fontSize: textPixels * 0.6
                        };

                        return (
                            <tspan>
                                <tspan className="value" style={valueStyle}>{value}</tspan>
                                <tspan style={percentStyle}>{props.percent}</tspan>
                            </tspan>
                        );
                    }}
                    riseAnimation
                    waveAnimation
                    waveFrequency={2}
                    waveAmplitude={1}
                    gradient
                    gradientStops={gradientStops}
                    circleStyle={{
                        fill: fillColor
                    }}
                    waveStyle={{
                        fill: fillColor
                    }}
                    textStyle={{
                        fill: color('#444').toString(),
                        fontFamily: 'Arial'
                    }}
                    waveTextStyle={{
                        fill: color('#fff').toString(),
                        fontFamily: 'Arial'
                    }}
                />
                <div
                    style={{
                        margin: '20px auto',
                        width: 120
                    }}
                >

                </div>
                <h1>{this.props.title}</h1>
                {this.props.param === "Weight" &&
                    <button onClick={()=>{weightMax = this.state.value;console.log(weightMax);this.setState({value:100})}}>
                        Tare
                    </button>
                }
            </div>
        );
    }
}


export default Graph  