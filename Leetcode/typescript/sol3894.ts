// https://leetcode.com/problems/traffic-signal-color/

function trafficSignal(timer: number): string {
    switch(timer){
        case (0):
            return "Green";
        case (30):
            return "Orange";
    }

    return 30 < timer && timer <= 90? "Red":"Invalid"
};