#include <iostream>
using namespace std;
enum imageType
{
    LSAT,
    SPOT
};
class Image
{
public:
    virtual void draw() = 0; //定义接口纯虚函数
    static Image *findAndClone(imageType);

protected:
    virtual imageType returnType() = 0;
    virtual Image *clone() = 0;
    static void addPrototype(Image *image)
    {
        _prototypes[_nextSlot++] = image;
    }

private:
    static Image *_prototypes[10];
    static int _nextSlot;
};
Image *Image::_prototypes[10];
int Image::_nextSlot;
Image *Image::findAndClone(imageType type)
{
    for (int i = 0; i < _nextSlot; i++)
        if (_prototypes[i]->returnType() == type)
        {
            return _prototypes[i]->clone();
        }
        return _prototypes[0]->clone();
}

class LandSatImage : public Image
{
public:
    imageType returnType() { return LSAT; }
    void draw() { cout << "LandSatImage::draw" << _id << endl; }
    Image *clone() { return new LandSatImage(1); }

protected:
    LandSatImage(int dummy) { _id = _count++; }

private:
    static LandSatImage _landSatImage;
    LandSatImage() { addPrototype(this); }
    int _id;
    static int _count;
};
LandSatImage LandSatImage::_landSatImage;
int LandSatImage::_count;
int main()
{
    Image *temp = Image::findAndClone(LSAT);
    temp->draw();
    return 0;
};