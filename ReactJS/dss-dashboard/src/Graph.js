import React, { Component } from 'react'

import firebase from './firebase'

class Graph extends Component {
    constructor(props) {
        super(props);
        this.state = {
            d: 0
        }
    };

    componentDidMount() {
        const db = firebase.firestore();

        db.collection("sampleData").doc("sampleDoc").onSnapshot((doc) => {
            var data = doc.data()['Distance'];
            console.log(data);
            this.setState({
                d: data
            });
        });
    };

    render() {
        if (this.state.d < 3) {
            return (
                <div>
                    {this.state.d}
                </div>
            );
        } else {
            return (
                <div style={{backgroundColor:'red'}}>
                    {this.state.d}
                </div>
            );
        }
    };
}


export default Graph  