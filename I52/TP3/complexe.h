#ifndef COMPLEXE_H
#define COMPLEXE_H

class Complexe
{
private:
    float re;
    float im;

public:
    Complexe(){re = 0.0, im = 0.0;};
    Complexe(float, float);    
    Complexe(const Complexe&);
    void print();
    ~Complexe();
    float getre();
    float getim();
    Complexe sum(const Complexe&);
    bool identical(const Complexe&);
    void Sum1(const Complexe&);
    Complexe Sum2(const Complexe&);
    Complexe Sum3(const Complexe&);
    Complexe& Sum4(const Complexe&);
};

#endif