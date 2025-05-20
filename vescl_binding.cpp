#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/numpy.h>
#include "Model/Model.h"
#include "Model/Curve.h"
#include "Model/Image.h"
#include "Model/ImageFilterer.h"
#include "View/RenderState.h"

namespace py = pybind11;

class VesselContouring {
public:
    VesselContouring() {
        m_renderState = new RenderState();
        m_model = new Model(m_renderState);
    }

    ~VesselContouring() {
        delete m_model;
        delete m_renderState;
    }

    void loadImage(const std::string& filename) {
        m_model->image().load(filename);
    }

    void startDraw(float x, float y, float radius) {
        CurvePoint point(Math::Vec2D(x, y), radius);
        m_model->startDraw(point);
    }

    void updateDraw(float x, float y, float radius) {
        CurvePoint point(Math::Vec2D(x, y), radius);
        m_model->updateDraw(point);
    }

    void endDraw(float x, float y, float radius) {
        CurvePoint point(Math::Vec2D(x, y), radius);
        m_model->endDraw(point);
    }

    void fitSelectedToVessel(float expectedRadius) {
        m_model->fitSelectedToNearestVessel(expectedRadius);
    }

    void fitSelectedVesselWidth(float expectedRadius) {
        m_model->fitSelectedVesselWidth(expectedRadius);
    }

    py::array_t<float> getRenderedImage(int width, int height) {
        // Create numpy array for the rendered image
        auto result = py::array_t<float>({height, width, 4});
        auto buf = result.request();
        float* ptr = (float*)buf.ptr;

        // Get the rendered image from the model
        // Note: You'll need to implement the actual rendering logic here
        // This is a placeholder that returns a blank image
        for (int i = 0; i < height * width * 4; i++) {
            ptr[i] = 0.0f;
        }

        return result;
    }

private:
    Model* m_model;
    RenderState* m_renderState;
};

PYBIND11_MODULE(vescl_binding, m) {
    py::class_<VesselContouring>(m, "VesselContouring")
        .def(py::init<>())
        .def("loadImage", &VesselContouring::loadImage)
        .def("startDraw", &VesselContouring::startDraw)
        .def("updateDraw", &VesselContouring::updateDraw)
        .def("endDraw", &VesselContouring::endDraw)
        .def("fitSelectedToVessel", &VesselContouring::fitSelectedToVessel)
        .def("fitSelectedVesselWidth", &VesselContouring::fitSelectedVesselWidth)
        .def("getRenderedImage", &VesselContouring::getRenderedImage);
} 